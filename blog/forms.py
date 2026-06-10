from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'content'
        ]
        labels = {
            'name': 'Họ và tên',
            'content': 'Bình luận'
        }