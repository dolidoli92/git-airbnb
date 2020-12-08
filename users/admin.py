from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# decorator : admin.site.register(models.User, CustomUserAdmin)
# is same to writing it below this function
@admin.register(models.User)
class CustomeUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
