from .models import Product
from django.forms import ModelForm, TextInput, NumberInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'comment']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название продукта',
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену продукта',
            }),
            'quantity': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество',
            }),
            'comment': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
            }),
        }
