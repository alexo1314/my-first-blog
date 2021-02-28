from django import forms

from .models import Post, About, Contacto


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'imagen')


class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = ('title', 'text')


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ('name', 'email', 'text')

