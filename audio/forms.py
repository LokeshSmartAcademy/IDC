from django import forms
from .models import StudentEnroll, SchoolEnroll


class StuEnroll(forms.ModelForm):
    class Meta:
        model = StudentEnroll
        fields = {'stuname', 'stuclass', 'stuschool', 'stucontact', 'stuemail', 'stutown' }

class SclEnroll(forms.ModelForm):
    class Meta:
        model = SchoolEnroll
        fields = {'sclname', 'scladdress', 'scltown', 'sclcontact', 'sclemail', 'scltown'}

