from django import forms
from ghost_post.models import *

class PostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}),max_length=280)
    is_boast = forms.ChoiceField(widget=forms.RadioSelect, choices=[('1', True), ('2', False)])