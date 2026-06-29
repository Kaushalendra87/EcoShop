from django import forms
from .models import Product

INPUT_CLASSES = (
    'w-full rounded-md border border-zinc-300 bg-white px-3 py-2 text-sm text-zinc-950 '
    'outline-none transition focus:border-emerald-500 focus:ring-2 focus:ring-emerald-100'
)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image', 'stock', 'active']
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Product Name'}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Price (e.g. 99.99)'}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES, 'placeholder': 'Product Description', 'rows': 4}),
            'image': forms.FileInput(attrs={'class': 'block w-full text-sm text-zinc-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-emerald-50 file:text-emerald-700 hover:file:bg-emerald-100'}),
            'stock': forms.NumberInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Stock Quantity'}),
            'active': forms.CheckboxInput(attrs={'class': 'h-4 w-4 rounded border-zinc-300 text-emerald-600 focus:ring-emerald-500'}),
        }
