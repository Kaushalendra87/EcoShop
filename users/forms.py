from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

INPUT_CLASSES = (
    'w-full rounded-md border border-zinc-300 bg-white px-3 py-2 text-sm text-zinc-950 '
    'outline-none transition focus:border-emerald-500 focus:ring-2 focus:ring-emerald-100'
)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': INPUT_CLASSES})

        self.fields['email'].required = True
        self.fields['username'].widget.attrs.update({'placeholder': 'Choose a username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'you@example.com'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Create a strong password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': INPUT_CLASSES})

        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})


class StyledPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(StyledPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': INPUT_CLASSES,
            'placeholder': 'Enter your account email',
        })


class StyledSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(StyledSetPasswordForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': INPUT_CLASSES})

        self.fields['new_password1'].widget.attrs.update({'placeholder': 'New password'})
        self.fields['new_password2'].widget.attrs.update({'placeholder': 'Confirm new password'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'first_name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'you@example.com'}),
        }

