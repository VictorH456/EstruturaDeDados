import random
from Menu import *
from Ranking import *
from Arquivo import *

def Selecao_tema():
    global palavras
    global pessoa
    #cadastro do jogador.
    pessoa = str(input("""\n-- Cadastro do Jogador --
Nome: """))

    while True:
        print("""\n### Temas ###
[1] Animais
[2] Frutas
[3] Objetos
[4] Pokemon\n""")
        #Escolha dos temas com try e except para caso ocorra algum erro o código continue funcionando
        try:
            escolha = int(input("Escolha o Tema: "))
            match escolha:
                case 1:
                    return arquivo("Animais.txt")
                case 2:
                    return arquivo("Frutas.txt")
                    
                case 3:
                    return arquivo("Objetos.txt")
                case 4:
                    return arquivo("Pokemon.txt")
            
        except:
            print("\nOcorreu algum erro")

def desenho_forca(x,y):
    #Apenas desenho da forca a cada tentativa.
    print(f"### JOGO FORCA ###             Palavra[{x}/{y}]")
    match tentativas:
        case 0:
            print("""---------------
|             |
|
|
|
|                  
|
|
|
-""")
        case 1:
            print("""---------------
|             |
|             0
|
|
|                  
|
|
|
-""")
        case 2:
            print("""---------------
|             |
|             0
|             |
|
|                  
|
|
|
-""")
        case 3:
            print("""---------------
|             |
|             0
|            -|
|
|                  
|
|
|
-""")
        case 4:
            print("""---------------
|             |
|             0
|            -|-
|
|                  
|
|
|
-""")
        case 5:
            print(f"""---------------
|             |
|             0
|            -|-
|            (
|                  
|
|
|
-""")
        case 6:
            print("""---------------
|             |
|             0
|            -|-
|            ( )
|                  
|
|
|      Perdeu o game!
-""")
    
def Play(palavras):
    global pontuacao
    global tentativas
    quantidade_de_palavras_total = len(palavras)
    pontuacao = 0
    quantidade_de_palavras_escolhidas = 0
    chute = ""
    verificacao = True
    
    
    #While do Play
    while(verificacao):
        global contagem
        tentativas = 0
        palavra = random.choice(palavras)
        palavras.remove(palavra)
        quantidade_de_palavras_escolhidas += 1
        palavra_escondida = []
        palavra = palavra.lower()
        verificacao_2 = True

        for i in range(len(palavra)):
            palavra_escondida.append("-")
        i = 0
        #while onde ocorre o jogo com a palavra sorteada
        while(verificacao_2):
            desenho_forca(quantidade_de_palavras_escolhidas,quantidade_de_palavras_total)
            
            #caso não chegue a 6 tentativass o jogo continua
            if tentativas != 6:
                print(f"\nJOGADOR: [{pessoa}]")
                print("Adivinhe: ")
                for i in range(len(palavra)):
                    if chute == palavra[i]:
                        palavra_escondida[i] = chute
                        if "".join(palavra_escondida) == palavra:
                            print(f"Acertou! - Palavra era: {palavra}")
                            pontuacao += 1
                            verificacao_2 = False
                print(" ".join(palavra_escondida))
            else:
                #Caso chegue a 6 tentativas mostra a palavra, pontuação e termina o laço.
                print(f"""\n A palavra era: {palavra}
\nSua pontuação(Quantidade de acertos): {pontuacao}""") 
                ranking[pessoa] = pontuacao
                verificacao = False
                break
            #verificação para caso a pessoa ganhe(Coloquei, porque não estava terminando o jogo antes de terminar o while)
            if verificacao_2 == False: break 
            
            if chute not in palavra:
                tentativas +=1

            chute = str(input("\nLetra: "))
            chute = chute.lower()