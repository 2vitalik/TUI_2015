# coding: utf-8
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm


class CustomUserChangeForm(UserChangeForm):
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 6:
            raise forms.ValidationError(u'Ви ввели занадто короткий пароль. Мінімальна довжина паролю 6 символів')
        return password1

class CustomUserCreationForm(UserCreationForm):
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 6:
            raise forms.ValidationError(u'Ви ввели занадто короткий пароль. Мінімальна довжина паролю 6 символів')
        return password1


class CustomAdminPasswordChangeForm(AdminPasswordChangeForm):
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 6:
            raise forms.ValidationError(u'Ви ввели занадто короткий пароль. Мінімальна довжина паролю 6 символів')
        return password1