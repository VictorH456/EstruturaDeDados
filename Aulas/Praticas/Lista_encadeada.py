class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

    def mostra_node(self):
        print(self.valor, end= " ")

class Lista_Encadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add_inicio(self, valor):
        #criando Nó
        newNode = Node(valor)
        newNode.next = self.inicio
        self.inicio = newNode

    def add_final(self, valor):
        #criando Nó
        newNode = Node(valor)
        if self.inicio == None:
            self.inicio = newNode
        else:
            self.fim.next = newNode
        self.fim = newNode

    def imprimir_lista(self):
        if self.inicio == None:
            print("-- Lista Vazia --")
            return None
        
        aux = self.inicio
        while aux != None:
            aux.mostra_node()
            aux = aux.next
        print("")


if __name__ == '__main__':
    L = Lista_Encadeada()
    L.add_inicio(10)
    L.add_inicio(20)
    L.add_inicio(30)
    L.imprimir_lista()

    L2 = Lista_Encadeada()
    L2.add_final(10)
    L2.add_final(20)
    L2.add_final(30)
    L2.imprimir_lista()