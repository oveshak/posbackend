from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Users, Roles, Branch


@admin.register(Roles)
class RolesAdmin(ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    filter_horizontal = ['menu']  # For many-to-many Group relation


@admin.register(Users)
class UsersAdmin(ModelAdmin):
    list_display = [
        'name', 'email', 'username', 'phone_number', 'branch',
        'roles', 'is_admin', 'is_staff', 'is_verified', 'status'
    ]
    search_fields = ['name', 'email', 'username', 'phone_number']
    list_filter = ['is_admin', 'is_staff', 'is_verified', 'status', 'branch', 'roles']
    readonly_fields = ['last_login']

    fieldsets = (
        (None, {
            'fields': (
                'email', 'username', 'name', 'phone_number', 'password', 'profile_picture',
                'roles', 'branch', 'address', 'descriptions',
                'nid_number', 'nid_front', 'nid_back'
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

@admin.register(Branch)
class BranchAdmin(ModelAdmin):
    list_display = ['name', 'address', 'phone', 'manager']
    search_fields = ['name', 'address', 'phone', 'manager__email']
    list_filter = ['manager']
