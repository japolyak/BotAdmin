from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _


# class UserAuthentication(forms.Form):
#     login = forms.CharField(max_length=255, label="Identifikator:", widget=forms.TextInput(attrs={'placeholder': 'Enter your identifikator'}))
#     password = forms.CharField(max_length=255, label="Password:", widget=forms.TextInput(attrs={'placeholder': 'Enter Password',
#                                                                                                 'type': 'password'}))

class UserAuthentication(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'placeholder': 'Enter Username'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', "autocomplete": "current-password"}),
    )


class UserSignupForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
