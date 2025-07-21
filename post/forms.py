from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control comment-textarea',
                'rows': 4,
                'placeholder': 'Write your comment here...',
            }),
        }