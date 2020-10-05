import re
from collections import Counter


def repeticao_palavras(lista_palavras):
    contagem_repeticao = Counter(lista_palavras).most_common()

    return contagem_repeticao


def le_assinatura():
    '''
    A funcao le os valores dos tracos linguisticos do modelo e devolve 
    uma assinatura a ser comparada com os textos fornecidos
    '''

    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''
    A funcao le todos os textos a serem comparados e devolve uma lista 
    contendo cada texto como um elemento
    '''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):")

    return textos


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
# FUNÇÕES PARA IMPLEMENTAR
#
#


def calcula_assinatura(texto):
    '''
    IMPLEMENTANDO. Essa funcao recebe um texto e deve devolver 
    a assinatura do texto.
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
    # print(lista_palavras)
    #print("Qtd palavras =",len(lista_palavras))

    # Imprime quantidade de palavras únicas
    #print("Qtd palavras únicas =", n_palavras_unicas(lista_palavras))

    # Imprime quantidade de palavras diferentes
    #print("Qtd palavras diferentes =", n_palavras_diferentes(lista_palavras))

    # Calcula o tamanho médio por palavra "wal_texto"
    # (Média simples do número de caracteres por palavra)
    caracter_palavras = 0
    for palavra in lista_palavras:
        caracter_palavras = caracter_palavras + len(palavra)
        # print(len(palavra))
    #print("Soma caracteres das palavras =",caracter_palavras)
    wal_texto = caracter_palavras / len(lista_palavras)
    wal_texto = abs(wal_texto)
    # print(wal_texto)

    # Calcula relação Type-Token "ttr_texto"
    # (Número de palavras diferentes utilizadas em
    # um texto divididas pelo total de palavras.)
    ttr_texto = n_palavras_diferentes(lista_palavras) / len(lista_palavras)
    # print(ttr_texto)

    # Calcula a razão Hapax Legomana "hlr_texto"
    # (Número de palavras utilizadas uma
    # vez dividido pelo número total de palavras.)
    hlr_texto = n_palavras_unicas(lista_palavras) / len(lista_palavras)
    # print(hlr_texto)

    # Calcula Tamanho médio de sentença "sal_texto"
    # (Média simples do número de caracteres por sentença)
    caracter_sentencas = 0
    for sentenca in lista_sentencas:
        caracter_sentencas = caracter_sentencas + len(sentenca)
    #print("Soma caracteres das sentenças =",caracter_sentencas)
    sal_texto = caracter_sentencas / len(lista_sentencas)
    # print(sal_texto)

    # Calcula Complexidade de sentença "sac_texto"
    # (Média simples do número de frases por sentença)
    sac_texto = len(lista_frases) / len(lista_sentencas)
    # print(sac_texto)

    # Calcula Tamanho médio de frase "pal_texto"
    # (Média simples do número de caracteres por frase)
    caracter_frases = 0
    for frase in lista_frases:
        caracter_frases = caracter_frases + len(frase)
    #print("Soma caracteres das frases =",caracter_frases)
    pal_texto = caracter_frases / len(lista_frases)
    # print(pal_texto)

    return(wal_texto, ttr_texto, hlr_texto, sal_texto, sac_texto, pal_texto)


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


def compara_assinatura(as_a, as_b):
    '''
    IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e 
    deve devolver o grau de similaridade nas assinaturas.
    '''

    i = 0
    ass_sim = 0
    while i < len(as_a):
        ass_sim = ass_sim + abs(as_a[i] - as_b[i])
        i = i + 1
    sab = abs(ass_sim)

    sab = sab / 6
    return(sab)

    '''
    soma_as_a = 0
    soma_as_b = 0
    for valor in as_a:
        soma_as_a = soma_as_a + valor
    
    for valor in as_b:
        soma_as_b = soma_as_b + valor

    sab = abs(soma_as_a - soma_as_b)
    sab = sab / 6    
    #print("SAB =", sab)
    return(sab)
    '''


def avalia_textos(textos, ass_cp):
    '''
    IMPLEMENTANDO. Essa funcao recebe uma lista de textos e uma 
    assinatura ass_cp e deve devolver o numero (1 a n) do texto com 
    maior probabilidade de ter sido infectado por COH-PIAH.
    '''

    sab = 100000
    i = 0

    while i < len(textos):
        ass_a = list(calcula_assinatura(textos[i]))
        # print(ass_a)
        sab_aux = compara_assinatura(ass_a, ass_cp)
        if sab_aux < sab:
            sab = sab_aux
            indice_texto = i + 1

        i = i + 1
    return(indice_texto)

######################
# Inìcio


def main():

    #textos = le_textos()
    #qtd_textos = len(textos)
    #i = 0
    # while i < qtd_textos:
    #    resultado = calcula_assinatura(textos[i])
    #    print(resultado)
    #    i = i + 1

    # Modificaçao

    ass_cp = le_assinatura()
    textos = le_textos()
    indice_texto = avalia_textos(textos, ass_cp)

    print(
        "O autor do texto", indice_texto, "está infectado com COH-PIAH"
    )


if __name__ == "__main__":
    main()
