from django import forms
from .models import DummyDB, StoreOtp

class ContactForm(forms.Form):
    print("helloooo-5")
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.ChoiceField(choices=[('telugu', 'Telugu'), ('hindi', 'HINDI'), ('english', 'English')])
    data = forms.CharField(widget=forms.Textarea)

class SnippetForm(forms.ModelForm):
    print("heloooo-6")
    class Meta:
        model = DummyDB
        fields = {'name', 'data', 'subject', 'email'}

class StoreOTPForm(forms.ModelForm):
    class Meta:
        model = StoreOtp
        fields = {'name', 'otp'}