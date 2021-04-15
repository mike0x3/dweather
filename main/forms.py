from django import forms

class searchCity(forms.Form):
	city = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Inserisci localita','type':'text'}))