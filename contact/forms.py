from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]
        
        labels = {
            'name': 'Họ và tên',
            'email': 'Email',
            'subject': 'Tiêu đề',
            'message': 'Nội dung'
        }