class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        self.ant = None

class Stack:
    def __init__(self):
        self.topo = None
        self.qt_c = 0  # Contador colchetes
        self.qt_p = 0  # Contador parenteses
        self.qt_ch = 0 # Contador chaves
        self.cont_negativo = False

    def push(self, valor):
        for i in valor:
            #Verifica equivalência
            if i == "(":
                self.qt_p += 1
            elif i == ")":
                self.qt_p -= 1
            if i == "{":
                self.qt_ch += 1
            elif i == "}":
                self.qt_ch -= 1
            if i == "[":
                self.qt_c += 1
            elif i == "]":
                self.qt_c -= 1
            #se ficar menor que 0 significa que não tá balanceada, pois coloquei um ),} ou ].
            if self.qt_p < 0 or self.qt_c < 0 or self.qt_ch < 0:
                self.cont_negativo = True
            
            newNode = Node(i)
            if self.topo is None:
                self.topo = newNode
            else:
                newNode.ant = self.topo
                self.topo.next = newNode
                self.topo = newNode

    def balanced(self):
        if self.qt_c==0==self.qt_p==self.qt_ch and self.cont_negativo == False:
            print("Balanceada")
        else:
            print("Não Balanceada")

if __name__ == "__main__":
    stack = Stack()
    stack.push("([])(){}(())()()")
    stack.balanced()