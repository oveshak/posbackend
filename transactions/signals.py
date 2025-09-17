from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta, date, timezone
from dateutil.relativedelta import relativedelta
from .models import Loan, Installment

def get_next_valid_date(current_date):
    while current_date.weekday() == 4:  # skip Friday
        current_date += timedelta(days=1)
    return current_date

def generate_installment_dates(start_date, installment_type):
    dates = []
    frequency = installment_type.type
    
    total_duration_months = installment_type.total_duration or 12
    print(total_duration_months  or 12)
    print(installment_type.instalment_cullect or 122 )
    print( installment_type.type)
    if frequency == "daily":
        total_installments = total_duration_months * 22
        delta = timedelta(days=installment_type.instalment_cullect)
    elif frequency == "weekly":
        total_installments = int(total_duration_months * 4.3)
        delta = timedelta(weeks=installment_type.instalment_cullect)
    elif frequency == "monthly":
        total_installments = total_duration_months
        delta = relativedelta(months=installment_type.instalment_cullect)
    elif frequency == "yearly":
        total_installments = max(1, total_duration_months // 12)
        delta = relativedelta(years=installment_type.instalment_cullect)
    else:
        return dates

    current_date = get_next_valid_date(start_date)
    for _ in range(total_installments):
        dates.append(current_date)
        current_date = get_next_valid_date(current_date + delta)
    return dates

@receiver(post_save, sender=Loan)
def create_installments(sender, instance, created, **kwargs):
    if not created:
        return

    print(f"\n--- Loan Created Debug ---")
    print(f"Loan ID: {instance.id}, Customer: {instance.customer_name}, Receive Type: {instance.receive_type}")
    print(f"Loan Amount: {instance.amount}, Installment Type: {getattr(instance.installment_type, 'type', 'N/A')}")
    print(f"First Down Payment: {instance.first_down_payment}")
    print(f"Loan Type: {getattr(instance.loan_type, 'name', 'N/A')}")

    # 🔹 Original Loan Amount
    original_amount = float(instance.amount)
    total_amount = original_amount

    # 🔹 LoanType behaviour_type calculation (percent = original_amount)
    if instance.loan_type and instance.loan_type.behaviour_type:
        print("Applying LoanType behaviour_type...")
        for item in instance.loan_type.behaviour_type:
            amt = float(item.get("amount", 0))
            if item.get("is_percent"):
                added = original_amount * amt / 100   # always original_amount
                total_amount += added
                print(f"  + {item['name']} (Percent {amt}%) => Added {added:.2f}")
            else:
                total_amount += amt
                print(f"  + {item['name']} (Fixed {amt}) => Added {amt:.2f}")

    print(f"Total Amount before Down Payment: {total_amount:.2f}")

    # 🔹 First Down Payment
    if instance.first_down_payment:
        total_amount -= float(instance.first_down_payment)
        total_amount = max(total_amount, 0)
        print(f"After First Down Payment Deduct: {total_amount:.2f}")

    # 🔹 InstallmentType check
    installment_type = instance.installment_type
    if not installment_type:
        print("No InstallmentType. Exiting.")
        return

    installment_amount = installment_type.instalment_cullect
    if not installment_amount or installment_amount <= 0:
        print("Invalid Installment Amount. Exiting.")
        return

    # 🔹 Generate installment dates
    start_date = date.today()
    dates = generate_installment_dates(start_date, installment_type)
    if not dates:
        print("No Installment Dates. Exiting.")
        return

    print(f"Generating {len(dates)} Installments (approx)")

    # 🔹 Create installments
    num_installments = len(dates)
    per_installment_amount = round(total_amount / num_installments, 2)
    remaining_amount = total_amount
    installments = []

    for i, inst_date in enumerate(dates):
        if i == num_installments - 1:
            amount = round(remaining_amount, 2)
        else:
            amount = per_installment_amount
            remaining_amount -= amount

        if amount <= 0:
            break

        installment = Installment.objects.create(
            customer_name=instance.customer_name,
            installment_date=inst_date,
            amount=amount,
            installment_status="due",
            area_name=instance.area_name,
            branch_name=instance.branch_name,
            loan_id=instance.id
        )
        installments.append(installment)
        print(f"  Installment {i+1}: Date={inst_date}, Amount={amount:.2f}, Remaining={remaining_amount:.2f}")

    if installments:
        instance.installment.set(installments, clear=True)
        print(f"{len(installments)} installments attached to Loan ID {instance.id}")

    # 🔹 Update updated_at
    if hasattr(instance, "updated_at"):
        Loan.objects.filter(pk=instance.pk).update(updated_at=timezone.now())
