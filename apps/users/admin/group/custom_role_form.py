from django import forms
from django.contrib.auth.models import Group


class CustomRoleForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "permissions"]
