from django import forms
from ckeditor.widgets import CKEditorWidget



class NewsletterForm(forms.Form):
    subject = forms.CharField(label="Asunto")
    receivers = forms.CharField(label="Dirigido a")
    message = forms.CharField(widget=CKEditorWidget(), label="Mensaje")

    