class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        self.ant = None

class Stack:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        for i in valor:
            newNode = Node(i)

            if self.topo == None:
                self.topo = newNode
            else:
                newNode.ant = self.topo
                self.topo.next = newNode
                self.topo = newNode

    def pop(self):
        pass

    def peek(self):
        pass

    def imprimir_stack(self):
        aux = self.topo
        if aux == None:
            print("Pilha vazia")
        else:
            while aux != None:
                print(f"{aux.valor}", end=" ")
                aux = aux.ant
            print()

if __name__ == "__main__":
    stack = Stack()
    stack.push("Olá Mundo!")
    stack.imprimir_stack()