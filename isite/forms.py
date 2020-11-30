from tinymce.models import HTMLField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Post, Page, Category


class PostForm(forms.ModelForm):
    text = HTMLField()

    class Meta:
        model = Post
        fields = ['title', 'text', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Отправить', css_class='form-submit'))

        self.helper.form_class = 'comment-form'
        self.helper.label_class = 'comment-form-comment'