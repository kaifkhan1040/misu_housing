from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import EmailTemplate

class EmailTemplateForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = EmailTemplate
        fields = ('body',)