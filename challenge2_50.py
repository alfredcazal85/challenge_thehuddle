def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejemplo de uso
lista_a_ordenar = [2000, 100, 45, 33, 22]
lista_ordenada = ordenamiento_burbuja(lista_a_ordenar)
print(f"Lista ordenada: {lista_ordenada}")
