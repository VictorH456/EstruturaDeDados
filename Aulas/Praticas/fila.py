class Fila:
    def __init__(self, size = 100):
        self.q = [None] * size
        self.capacidade = size
        self.inicio = -1
        self.fim = -1
        self.count = 0

    def enqueue(self, value):
        if self.isFull():
            print("Overflow, Fila está cheia.")
            exit(-1)
        elif self.isEmpty():
            print("inserindo elemento: ", value)
            self.fim += 1
            self.inicio += 1
        else:
            print("inserindo elemento: ", value)
            self.fim += 1

        self.q[self.fim] = value
        self.count += 1

    def denqueue(self, value):
        if self.isEmpty():
            print("Não posso desenfileirar uma pilha vazia")
            exit(-1)
        x = self.q[self.inicio]
        
        print("Removendo elemento: ", x)
        self.inicio += 1
        self.count -= 1

    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.capacidade 

    def imprimir_fila(self):
        if self.isEmpty():
            print("Lista vazia")
        else:
            for i in self.q:
                if i != None:
                    print(f"[{i}]",end=" ")
            print()
            
if __name__ == "__main__":
    fila = Fila(4)
    fila.imprimir_fila()
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)
    fila.enqueue(40)
    fila.enqueue(50)
    fila.imprimir_fila()