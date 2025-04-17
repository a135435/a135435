from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """用于创建新用户的表单"""
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    """用于更新用户信息的表单"""
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'avatar', 'position', 'organization')


class ProfileUpdateForm(forms.ModelForm):
    """用户个人资料更新表单"""
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'bio', 'avatar', 'position', 'organization')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }