from django import forms
from cloudmeb.websites.models import Website

class WebsiteForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = Website
        fields = '__all__'
        widgets = {'smtp_password': forms.PasswordInput(render_value=True),}