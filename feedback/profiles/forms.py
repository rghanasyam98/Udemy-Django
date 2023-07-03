from django import forms

class ProfileForm(forms.Form):
    user_image=forms.FileField(allow_empty_file=False,required=True)#can also use ImageField