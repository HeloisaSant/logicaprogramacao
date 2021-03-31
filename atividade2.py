
def calcula_soma(lista_de_numeros):
    soma = 0
    for numero in lista_de_numeros:
        soma = soma + numero

    return soma

print(calcula_soma([3,8,9,2,0]))


def converte_entrada(texto):
        lista = texto.split(' ')
        listaInteiros = []
        for numero in lista:
            listaInteiros.append(int(numero))
        return listaInteiros

print(converte_entrada("3 8 9 2 0"))


def processa_numeros(lista_elementos):
    soma = 0
    for numero in lista_elementos:
        soma = soma + numero

    return (soma,len(lista_elementos))

print(processa_numeros([27,22,7]))


def main():
    numeros = raw_input("digite um conjunto de numeros separados por espaco")

    listaNumeros = converte_entrada(numeros)
    

    soma, quantidade = processa_numeros(listaNumeros)

    media = soma / quantidade

    return media

print(main())
