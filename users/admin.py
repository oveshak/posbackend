from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Area, Users, Roles, Branch


@admin.register(Roles)
class RolesAdmin(ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    filter_horizontal = ['menu']  # For many-to-many Group relation


@admin.register(Users)
class UsersAdmin(ModelAdmin):
    list_display = [
        'name', 'email', 'username', 'phone_number', 'branch',
        'roles', 'is_admin', 'is_staff', 'is_verified', 'status','area'
    ]
    search_fields = ['name', 'email', 'username', 'phone_number']
    list_filter = ['is_admin', 'is_staff', 'is_verified', 'status', 'branch', 'roles','area']
    readonly_fields = ['last_login']

    fieldsets = (
        (None, {
            'fields': (
                'email', 'username', 'name', 'phone_number', 'password', 'profile_picture',
                'roles', 'branch', 'address', 'descriptions',
                'nid_number', 'nid_front', 'nid_back','area'
            )
        }),
        ('Permissions', {
            'fields': ('is_admin', 'is_staff', 'is_verified', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Status', {
            'fields': ('status', 'created_at', 'is_deleted', 'last_login')
        }),
    )

    def save_model(self, request, obj, form, change):
        raw_password = form.cleaned_data.get("password")
        if raw_password and not raw_password.startswith('pbkdf2_'):
            obj.set_password(raw_password)  # ⬅️ hash the password properly
        super().save_model(request, obj, form, change)
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']   # area_staf M2M, তাই list_display তে ডাইরেক্ট দেখানো যাবে না
    search_fields = ['name', 'address', 'area_staf__email']
    # list_filter = ['manager']  # Area model এ manager নাই, তাই বাদ দিলাম

    # M2M ফিল্ড admin এ দেখাতে চাইলে কাস্টম মেথড বানাতে হবে
    def get_area_stafs(self, obj):
        return ", ".join([user.email for user in obj.area_staf.all()])
    get_area_stafs.short_description = "Area Staff"


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'manager']  # total_area M2M, তাই ডাইরেক্ট রাখা যাবে না
    search_fields = ['name', 'address', 'phone', 'manager__email', 'total_area__name']
    list_filter = ['manager']

    # total_area দেখানোর জন্য কাস্টম মেথড
    def get_total_areas(self, obj):
        return ", ".join([area.name for area in obj.total_area.all()])
    get_total_areas.short_description = "Total Areas"

