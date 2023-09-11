def Busca_sequencia(lista, num):
    pos = []
    
    for i in range(len(lista)):
        if lista[i] == num:
            pos.append(i)
    return pos

def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    
    resultado = []
    while inicio <= fim:
        meio = (inicio + fim) // 2 
        chute = lista[meio]
        
        # Caso encontre o item.
        if chute == item:
            resultado.insert(-1, meio) #insiro a posição do chute, ou seja, o meio achado.
            
            # Crio duas variaveis para a direita e esquerda, ou seja, maior e menor.
            mais = meio + 1
            menos = meio - 1
            
            # Laço onde ele verifica o valor da posição de menos.
            while True: 
                if lista[menos] == item: # Caso seja igual, ele adiciona no resultado e diminui novamente.
                    resultado.insert(-1, menos)
                    menos -= 1
                else:# Caso não seja igual, ele para o laço.
                    break
            
            # Laço onde ele verifica o valor da posição de mais.
            while True:
                if lista[mais] == item: # Caso seja igual, ele adiciona no resultado e diminui novamente.
                    resultado.append(mais) 
                    mais += 1
                else: # Caso não seja igual, ele para o laço.
                    break
            #Por fim ele retorna tudo.
            return resultado
        
        if chute < item:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    # Item não existe no conjunto, retorna vazio
    return resultado

lista = [4, 14, 15, 19, 21, 23, 45, 78, 81, 81, 90]
num = 81
print(Busca_sequencia(lista, num))
print(busca_binaria(lista, num))