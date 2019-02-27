from django import forms
from .models import BlogPost

class NewBlogForm(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = ['title', 'text']