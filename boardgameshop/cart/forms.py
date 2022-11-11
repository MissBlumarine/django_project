from django import forms
from boardgames.models import OrderItem


class AddQuantityForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']

