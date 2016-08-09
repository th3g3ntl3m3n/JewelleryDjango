from django import forms
from django.contrib.auth.models import User
from .models import ReviewProduct, ShoppingDetail

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']

class ReviewForm(forms.ModelForm):
	class Meta:
		model = ReviewProduct
		fields = ['review', 'rating']

class ShoppingDetailForm(forms.ModelForm):
    class Meta:
        model = ShoppingDetail
        fields = ['full_name', 'street', 'town', 'district', 'state', 'country', 'pin']
