from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import TextoForm
from .testes import *

#from django.http import HttpRequest


class IndexView(TemplateView):
    template_name = 'index.html'


def texto(request):
    form = TextoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():

            texto = form.get_texto()
            lista = devolve_listas(texto)
            sentecas = lista[0]
            frases = lista[1]
            palavras = lista[2]
            palavras_unicas = lista_palavras_unicas(palavras)
            palavras_diferentes = lista_palavras_diferentes(palavras)
            lista_repeticao = repeticao_palavras(palavras)

            num_sentencas = len(sentecas)
            num_frases = len(frases)
            num_palavras = len(palavras)
            num_palavras_unicas = n_palavras_unicas(palavras)
            num_palavras_diferentes = n_palavras_diferentes(palavras)

            form = TextoForm()

            context = {

                'relatorio': [
                    f'Número de sentenças => {num_sentencas}',
                    f'Número de frases => {num_frases}',
                    f'Total de palavras => {num_palavras}',
                    f'Número de palavras únicas => {num_palavras_unicas}',
                    f'Palavras únicas => {palavras_unicas}',
                    f'Número de palavras diferentes => {num_palavras_diferentes}',
                    f'Palavras diferentes => {palavras_diferentes}',
                    f'Repetição das palavras => {lista_repeticao}',
                    f'Lista de palavras => {palavras}',
                ],
                'form': form

            }
            return render(request, 'texto.html', context)

    form = TextoForm()
    context = {
        'form': form
    }
    return render(request, 'texto.html', context)
