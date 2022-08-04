from django import forms
from django.dispatch import receiver
from pkg_resources import require
from .models import Message, Post,Comment, ThreadModel

class PostForm(forms.ModelForm):
    body = forms.CharField(label='',widget=forms.Textarea(attrs={
        'rows':3,
        'placeholder':'Post Something...'
    }))

    image = forms.ImageField(required=False,widget=forms.ClearableFileInput(attrs={
        'multiple':True
    }))

    class Meta:
        model = Post
        fields = ['body']
    


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='',widget=forms.Textarea(attrs={
        'rows':3,
        'placeholder':'Comment Something...Anything...'
    }))

    image = forms.ImageField(required=False)

    class Meta:
        model = Comment
        fields = ['comment','image']

class ThreadForm(forms.Form):
    username = forms.CharField(label='',max_length=100)

class MessageForm(forms.ModelForm):
    body = forms.CharField(label='',max_length=1000)
    image = forms.ImageField(required=False)

    class Meta:
        model = Message
        fields = ['body','image']

class ShareForm(forms.Form):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows':'3',
            'placeholder':'Post Something....',
        })
    )

class ExploreForm(forms.Form):
    query = forms.CharField(label='',
    widget=forms.TextInput(attrs={
        'placeholder':'Explore Tags'
    }))