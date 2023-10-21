from django import forms
from .models import User, Group


class UserForm(forms.ModelForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
        empty_label="Select your group"
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'group', 'created']
        exclude = ['created']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control py-4', 'placeholder': 'Enter your email'}),
        }
