from Imports import *

while(True):
    while True:
        try:
            Menu()
            opcao = int(input("Qual a sua escolha: "))
            break
        except:
            print("\nOcorreu algum erro, tente novamente")
    match opcao:
        case 1:
            Play(Selecao_tema())
        case 2:
            Ranking()
        case 3:
            break
    