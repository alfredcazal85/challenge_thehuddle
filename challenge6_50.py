class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecha, valor)

    def inorden(self, nodo_actual):
        if nodo_actual is not None:
            self.inorden(nodo_actual.izquierda)
            print(nodo_actual.valor, end=' ')
            self.inorden(nodo_actual.derecha)

# Crear el árbol y insertar 5 elementos
arbol = ArbolBinarioBusqueda()
elementos = [10, 5, 20, 3, 7]

for elem in elementos:
    arbol.insertar(elem)

# Imprimir el árbol en orden para verificar la inserción
print("Elementos del BST en orden:")
arbol.inorden(arbol.raiz)
