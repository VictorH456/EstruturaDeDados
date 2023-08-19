#Função para ler as palvras da Opção desejada
#Basicamento abro o arquivo leio ele e transformo em uma lista
def arquivo(nome_arquivo):
    global palavras
    with open(nome_arquivo, 'r') as arquivo:
        palavras = arquivo.read().split('\n')
        return palavras