from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': '',
        }
        widgets = {
            'body': forms.Textarea(attrs={
                                    'rows': 5, 
                                    'placeholder': 'Leave a comment here',
                                    'id': 'body-id',
                                    'required': True,
            }),
        }