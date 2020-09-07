def contar_caracteres(texto):
    """ Função que conta os caracteres de uma string
    Ex:
    >>> contar_caracteres('wagner')
    {'a': 1 'e': 1 'g': 1 'n': 1 'r': 1 'w': 1}

    >>> contar_caracteres('banana')
    {'a': 3 'b': 1 'n': 2}
    :param texto: string a ser contada
    """
    resultado = {}
    for caracter in sorted(texto):
        resultado[caracter] = resultado.get(caracter, 0) + 1
    return resultado


print(contar_caracteres('wagner'))
print()
print(contar_caracteres('banana'))
