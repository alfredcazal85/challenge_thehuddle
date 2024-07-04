def eliminar_duplicados(lista):
    # Usar un conjunto para eliminar duplicados
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

# Lista de 10 enteros con duplicados
lista = [1, 2, 3, 2, 4, 5, 6, 3, 7, 8]

# Eliminar duplicados
resultado = eliminar_duplicados(lista)
print("Lista original:", lista)
print("Lista sin duplicados:", resultado)
