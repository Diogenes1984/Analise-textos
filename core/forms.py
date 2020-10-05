from django import forms


class TextoForm(forms.Form):
    texto = forms.CharField(label='Texto', widget=forms.Textarea())

    def get_texto(self):
        texto = self.cleaned_data['texto']
        return texto
