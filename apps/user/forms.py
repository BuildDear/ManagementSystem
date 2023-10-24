from django import forms
from .models import User, Group


class UserForm(forms.ModelForm):
    first_name = forms.CharField(min_length=2, max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                               'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(min_length=2, max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                              'placeholder': 'Enter your last name'}))

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
            'email': forms.EmailInput(attrs={'class': 'form-control py-4',
                                             'placeholder': 'Enter your email'}),
        }


class GroupForm(forms.ModelForm):
    name = forms.CharField(min_length=3, max_length=20,
                           widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                         'placeholder': 'Enter a group name'}))
    description = forms.CharField(min_length=5, max_length=20,
                                  widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                                'placeholder': 'Enter a description'}))

    class Meta:
        model = Group
        fields = ['name', 'description']
        exclude = ['users_count']

