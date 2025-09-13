from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Customer, CustomerGroup, Contact

@admin.register(CustomerGroup)
class CustomerGroupAdmin(ModelAdmin):
    list_display = ("id", "name", "group_leader_user", "created_at")  # removed updated_at, is_active
    search_fields = ("name", "group_leader_user__email", "group_leader_user__name")
    list_filter = ("created_at",)  # removed is_active, updated_at
    raw_id_fields = ("group_leader_user",)

@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ("id", "type", "name", "email", "phone", "customer_group", "branch_name", "created_at")  # removed updated_at, is_active
    search_fields = ("name", "email", "phone", "customer_group__name", "branch_name__name")
    list_filter = ("type", "customer_group", "branch_name", "created_at")  # removed is_active, updated_at
    raw_id_fields = ("customer_group", "branch_name")
@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "father_husband_name",
        "mobile_number",
        "secondary_mobile_number",
        "guarantor",
        "nid_number",
        "branch_name",
        "account_balance",
        "created_at"
    )
    search_fields = (
        "full_name",
        "father_husband_name",
        "mobile_number",
        "secondary_mobile_number",
        "nid_number",
        "guarantor__name",
        "branch_name__name"
    )
    list_filter = (
        "branch_name",
        "created_at"
    )
    raw_id_fields = (
        "guarantor",
        "branch_name"
    )
    readonly_fields = ("account_balance",)