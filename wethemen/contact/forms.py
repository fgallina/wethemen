from django import forms
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(label=_("Name"), max_length=100, required=True)
    email = forms.EmailField(label=_("Email"), required=True)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(
        label=_("Message"),
        required=True,
        widget=forms.widgets.Textarea(attrs={'rows':'25','cols':'5'})
    )
    cc_myself = forms.BooleanField(required=False)
