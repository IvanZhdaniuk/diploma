from django import forms
class QuestionForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    mobile_phone = forms.IntegerField(label='Your phone number')
    question = forms.CharField(widget=forms.Textarea)
