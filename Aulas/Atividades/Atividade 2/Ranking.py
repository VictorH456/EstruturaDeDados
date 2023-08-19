#Função Ranking: Ela serve para mostrar o ranking do jogo.
def Ranking():
    global ranking

    print("\n-- Ranking --\n")
    
    if len(ranking) > 1:
        #Essa basicamente ordena meu dicionario.
        ranking = dict(ranking.items(), key=lambda item: item[1], reverse=True)


    #enumerate: ele percorre a lista ranking junto das posições, ou seja,
    # Ele pega os valores dos elementos e suas posições, 
    # como dei start = 1, a contagem das posições começa do 1.
    for posicao, pessoa in enumerate(ranking, start = 1): 
        print(f"{posicao}. {pessoa}         {ranking[pessoa]} Acertos")
ranking = {}