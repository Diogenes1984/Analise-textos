import re
from collections import Counter


def repeticao_palavras(lista_palavras):
    contagem_repeticao = Counter(lista_palavras).most_common()

    return contagem_repeticao


def separa_sentencas(texto):
    '''
    A funcao recebe um texto e devolve uma lista das sentencas 
    dentro do texto
    '''

    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''
    A funcao recebe uma sentenca e devolve uma lista das frases 
    dentro da sentenca
    '''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''
    A funcao recebe uma frase e devolve uma lista das palavras 
    dentro da frase
    '''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''
    Essa funcao recebe uma lista de palavras e devolve o numero de 
    palavras que aparecem uma unica vez
    '''

    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def lista_palavras_unicas(lista_palavras):
    '''
    Essa funcao recebe uma lista de palavras e devolve uma lista de 
    palavras que aparecem uma unica vez
    '''

    freq = dict()
    unicas = 0
    lista_palavras_unicas = []
    for palavra in lista_palavras:
        p = palavra.lower()

        if p in freq:
            if freq[p] == 1:
                unicas -= 1

            freq[p] += 1

        else:
            freq[p] = 1
            lista_palavras_unicas.append(p)
            unicas += 1
    return lista_palavras_unicas


def n_palavras_diferentes(lista_palavras):
    '''
    Essa funcao recebe uma lista de palavras e devolve o numero de 
    palavras diferentes utilizadas
    '''

    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def lista_palavras_diferentes(lista_palavras):
    '''
    Essa funcao recebe uma lista de palavras e devolve uma lista de 
    palavras diferentes utilizadas
    '''

    freq = dict()
    lista_palavras_diferentes = []

    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
            lista_palavras_diferentes.append(p)

    return lista_palavras_diferentes


def devolve_listas(texto):
    '''
    IMPLEMENTANDO. Essa funcao recebe um texto e deve devolver Listas 
    de listas. 1° lista_sentencas 2° lista_frases 3° lista_palavras
    '''

    # Separa as sentenças em uma lista chamada "lista_sentenças"
    lista_sentencas = separa_sentencas(texto)
    # print(lista_sentencas)
    #print("Qtd sentenças =",len(lista_sentencas))

    # Separa as frases em uma lista chamada "lista_frases"
    lista_frases = []
    i = 0
    while i < len(lista_sentencas):
        frase = separa_frases(lista_sentencas[i])
        lista_frases.extend(frase)
        i = i + 1
    # print(lista_frases)
    #print("Qtd frases =",len(lista_frases))

    # Separa as palavras em uma lista chamada "lista_palavras"
    lista_palavras = []
    i = 0
    while i < len(lista_frases):
        palavras = separa_palavras(lista_frases[i])
        lista_palavras.extend(palavras)
        i = i + 1
    lista_palavras_lower_case = []
    for palavra in lista_palavras:
        p = palavra.lower()
        lista_palavras_lower_case.append(p)

    listas = []
    listas = [lista_sentencas, lista_frases, lista_palavras_lower_case]
    return listas
