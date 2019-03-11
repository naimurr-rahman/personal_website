from django import forms
from basic_app.models import Contact

class ContactForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                        'placeholder':'Whats your name'}))

    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                        'placeholder':'Enter your Email'}))

    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                        'placeholder':'Enter subject'}))

    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
                                                        'placeholder':'Enter your message'}))


    class Meta():
        model = Contact
        fields = ('name','email','subject','message')

    def __str__(self):
        return self.name
