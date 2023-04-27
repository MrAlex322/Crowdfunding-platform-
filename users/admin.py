from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from users.forms import UserCreationForm, NewsPostForm
from .models import NewsPost

User = get_user_model()


class MyUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", 'email', "password1", "password2"),
            },
        ),
    )
    add_form = UserCreationForm


admin.site.register(User, MyUserAdmin)



