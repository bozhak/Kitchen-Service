from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import DishType, Dish


User = get_user_model()


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"


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


class CookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder":"Search by username, First Name or Last Name"}
        )
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

    def clean_price(self):
        price = self.cleaned_data.get("price")
        return validate_dish_field(price)

    def clean_description(self):
        description = self.cleaned_data.get("description")
        return validate_description_field(description)


def validate_description_field(description):
    description = str(description)
    if description < 20:
        return ValidationError("Length must be more than 20.")


def validate_dish_field(price):
    if price is None:
        return price

    if price < 0:
        raise ValidationError("Price must be more than 0.")

    # description = str(description)

    # if len(description) < 20:
    #     raise ValidationError("Length of description must be more than 20")

    return price


class DishSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder":"Search by name or dish type"}
        )
    )


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
