from django import forms
from .models import Mentor

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('name', 'email', 'price')
