def contar_caracteres(texto):
    """ Função que conta os caracteres de uma string
    Ex:
    >>> contar_caracteres('wagner')
    a: 1
    e: 1
    g: 1
    n: 1
    r: 1
    w: 1
    >>> contar_caracteres('banana')
    a: 3
    b: 1
    n: 2

    :param texto: string a ser contada
    """
    caracteres_ordenados = sorted(texto)
    caracter_anterior = caracteres_ordenados[0]
    contagem = 1
    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            contagem = 1
            caracter_anterior = caracter
    print(f'{caracter_anterior}: {contagem}')


contar_caracteres('wagner')
print()
contar_caracteres('banana')
