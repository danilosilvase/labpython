if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    cont = -1
    lista = list(arr)
    lista.sort()
    last = lista[cont-1]
    if last == lista[cont]:
        while last == lista[cont]:
            cont -= 1
    # cont -= 1
    print(lista[cont])