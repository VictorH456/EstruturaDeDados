class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        self.ant = None

class Stack:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        newNode = Node(valor)

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
                print(f"[{aux.valor}]")
                aux = aux.ant

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.imprimir_stack()