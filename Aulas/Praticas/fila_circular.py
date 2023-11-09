class FilaCircular:
    def __init__(self, maxSize):
        self.queue = list()
        self.maxSize = maxSize
        self.tail = -1
        self.head = -1

    def enQueue(self, data):
        if self.size() == self.maxSize:
            return ("Fila está cheia!")
        
        elif self.size() == 0:
            self.queue.append(data)
            self.tail = (self.tail +1) % self.maxSize
            self.head = (self.head +1) % self.maxSize

        else:
            self.queue.append(data)
            self.tail = (self.tail +1) % self.maxSize
            

    def size(self):
        if self.tail > self.head:
            return self.maxSize - ((self.tail - self.head)-1)
        else:     
            return (self.tail - self.head) + 1

if __name__ == "__main":
    filaCircular = FilaCircular(5)
    print(filaCircular.size())
    filaCircular.enQueue(10)