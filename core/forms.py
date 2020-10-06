from django import forms


class TextoForm(forms.Form):
    texto = forms.CharField(
        widget=forms.Textarea(),
        label='Digite ou cole o texto aqui',
    )

    def get_texto(self):
        texto = self.cleaned_data['texto']
        return texto
