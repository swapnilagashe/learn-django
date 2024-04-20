from django import forms
from .models import Menu

class DemoForm(forms.Form):
    name = forms.CharField(max_length=20)
    some_field = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    some_field_2 = forms.CharField(label = "enter something")
    number_input = forms.DateField()
    #choice_input = forms.ChoiceField()
    email  = forms.EmailField()
    age = forms.IntegerField()
    
class DemoModelForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
    
