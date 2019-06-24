from django import forms
from home.models import Book,Author,Genre

class BookForms(forms.Form):
    name=forms.CharField(
        label='book name',
        widget=forms.TextInput(
            attrs={'placeholder':'book name',
            'class':'forms-control' }
        )
    )
    pur_date=forms.DateField(label='',widget=forms.DateInput(attrs={'placeholder':'Purchase date','name':'purchase_date','id':'purchase_date','class':'form-control'}))
    

