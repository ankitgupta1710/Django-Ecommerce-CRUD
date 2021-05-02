from django import forms
from .models import Product, OFFERS, DELIVERY_OPTIONS


class ProductForm(forms.ModelForm):
    delivery_options = forms.ChoiceField(widget=forms.RadioSelect,choices= DELIVERY_OPTIONS)
    offers= forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OFFERS )
    
    class Meta:
        model = Product
        fields = '__all__'
       
        