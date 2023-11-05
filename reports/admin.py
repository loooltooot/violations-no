from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Report
from django.utils.translation import gettext_lazy as _

# Register your models here.

class ReportsInline(admin.TabularInline):
    model = Report
    extra = 0

class MyUserAdmin(UserAdmin):
    inlines = [
        ReportsInline,
    ]
    list_display = ['username', 'get_fio', 'tel']
    fieldsets = (
        (None, {
            'fields': [
                'username', 'email', 'password', 'last_login'
            ],
        }),
        (_('Personal information'), {
            'fields': [
                'last_name', 'first_name', 'patronymic', 'tel'
            ]
        }),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Personal information'), {'fields': ('last_name', 'first_name', 'patronymic', 'tel')}),
    )
    

admin.site.register(MyUser, MyUserAdmin)