from django import forms
from .models import Order

INPUT_CLASSES = (
    'w-full rounded-md border border-zinc-300 bg-white px-3 py-2 text-sm text-zinc-950 '
    'outline-none transition focus:border-emerald-500 focus:ring-2 focus:ring-emerald-100'
)

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'address', 'city', 'postal_code']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'you@example.com'}),
            'phone': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Phone Number'}),
            'address': forms.Textarea(attrs={'class': INPUT_CLASSES, 'placeholder': 'Delivery Address', 'rows': 3}),
            'city': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'City'}),
            'postal_code': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Postal / ZIP Code'}),
        }
