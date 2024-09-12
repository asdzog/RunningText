from django import forms


class TextForm(forms.Form):
    text = forms.CharField(label='Введите текст для бегущей строки', max_length=200)
