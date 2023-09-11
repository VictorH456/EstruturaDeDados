class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

    def mostra_node(self):
        print(self.valor, end="-> ")


class Lista_Encadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add_inicio(self, valor):
        newNode = Node(valor)
        newNode.next = self.inicio
        self.inicio = newNode

    def add_final_v1(self, valor=None):
        if (valor == None):
            print("Valor vazio!")
            return None
        newNode = Node(valor)
        if self.inicio == None:
            self.inicio = newNode
        else:
            aux = self.inicio
            while aux.next != None:
                aux = aux.next
            aux.next = newNode

    def add_final_v2(self, valor):
        newNode = Node(valor)
        if self.inicio == None:
            self.inicio = newNode
            self.fim = newNode
        else:
            self.fim.next = newNode
            self.fim = newNode

    def imprime_lista(self):
        if self.inicio == None:
            print("-- Lista Vazia --")
            return None
        aux = self.inicio
        while aux != None:
            aux.mostra_node()
            aux = aux.next
        print("")

# --------------------------------------- Exercício 03 - Lista Encadeada Simples.pdf
    def busca_simples(self, valor):
        # Implementar...
        pass


    def remover(self, valor):
        # Implementar...
        pass


if __name__ == '__main__':
    # ------------------------------ INSERÇÃO Números aleatórios

    L = Lista_Encadeada()
    print("Inserir 10 numeros aleatórios")
        # Implementar...


    L.imprime_lista()
    
    # ---- Teste do Exercício
    # ------------------------------ BUSCA
    valor_buscado = 64
    print(f"Buscar um item na lista ({valor_buscado})")
    nodeX = L.busca_simples(valor_buscado)
    #a if condition else b
    nodeX.mostra_node() if nodeX else print("Item não encontrado!")

    # ------------------------------ EXCLUIR
    valor_excluir = 64
    print(f"Elemento a ser excluído: ({valor_excluir})")
    nodeX = L.excluir(valor_excluir)
    nodeX.mostra_node() if nodeX else print("Item não encontrado!")
    print()
    L.imprime_lista()
