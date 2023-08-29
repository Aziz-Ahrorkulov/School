from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

class ProfilePicForm(forms.ModelForm):

    user_img = forms.ImageField(label='Profile Picture')

    class Meta:
        model = Profile
        fields = ('user_img',)

class SendForm(forms.Form):
    name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

# class SignUp(forms.ModelForm):
#     username : forms.TextInput(attrs={'class': 'form-control', 'id': 'inputFirstName','placaeholder': 'First Name'})
#     last_name : forms.TextInput(attrs={'class': 'form-control', 'id': 'inputLastName','placaeholder': 'Last Name'})
#     email : forms.EmailInput( attrs={'class': 'form-control', 'id': 'inputEmailAddress', 'placaeholder': 'Email'})
#     password : forms.TextInput( attrs={'class': 'form-control', 'id': 'inputPassword', 'placaeholder': 'Password'})
    

#     class Meta:
#         model = User
#         fields = ['username', 'last_name', 'email', 'password']


# class UserUpdateForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fileds = ['username', 'email', 'password', 'confirm_password']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fileds = ['user_img']


# forms.py


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'id' : 'inputFirstName','placeholde': 'First Name'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'id' : 'inputLastName','placeholde': 'Last Name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'id' : 'inputEmailAddress','placeholde': 'Email'}))
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id' : 'oldPassword', 'placeholde': 'Old Password'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control','id' : 'newPassword1','placeholde': 'New Password'}), required=False)
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class': 'form-control','id' : 'newPassword2','placeholde': 'Confirm Password'}), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if old_password and (not new_password1 or not new_password2):
            raise forms.ValidationError("Please enter a new password and confirm it.")

        if new_password1 != new_password2:
            raise forms.ValidationError("New passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')

        if old_password and new_password1:
            user.set_password(new_password1)

        if commit:
            user.save()

        return user
