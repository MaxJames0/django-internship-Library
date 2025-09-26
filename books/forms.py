from django import forms

from books.models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('created_at', 'updated_at', 'added_by')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        
        
class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        exclude = ('created_at',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentBook
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control mb-3',
                'rows': 5,
                'placeholder': 'Write your comment...'
            }),
        }