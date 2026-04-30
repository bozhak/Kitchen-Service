from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import DishType, Dish


User = get_user_model()


class CookCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )



class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Dish
        fields = "__all__"


#
# class DriverLicenseUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ("license_number",)
#
#     def clean_license_number(self):
#         return validate_license_number(
#             self.cleaned_data.get("license_number")
#         )
#
#
# def validate_license_number(license_number):
#     if not license_number:
#         return license_number
#
#     license_number = str(license_number)
#
#     if len(license_number) != 8:
#         raise ValidationError("License must be exactly 8 characters")
#
#     if not license_number[:3].isupper() or not license_number[:3].isalpha():
#         raise ValidationError(
#             "First 3 characters must be uppercase letters"
#         )
#
#     if not license_number[3:].isdigit():
#         raise ValidationError(
#             "Last 5 characters must be digits"
#         )
#
#     return license_number
