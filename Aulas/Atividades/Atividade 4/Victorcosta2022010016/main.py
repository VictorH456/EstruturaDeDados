#Aluno:Victor Hugo Souza Costa
#Matricula:2022010016

"""Não consegui fazer funcionar, mas adicionei um botão de restart,
onde ele limpa os montes e chama a função start_game(), também adicionei um temporizador 
que iria utilizar para a contagem dos pontos.

"""

from tkinter import *
import random
from PIL import Image, ImageTk
import time


# Variável para acompanhar o tempo inicial
tempo_inicial = None

# Função para atualizar o temporizador
def atualiza_tempo():
    if tempo_inicial is not None:
        tempo_decorrido = int(time.time() - tempo_inicial)
        minutos = tempo_decorrido // 60
        segundos = tempo_decorrido % 60
        tempo_str = f"Tempo: {minutos:02d}:{segundos:02d}"
        tempo_label.config(text=tempo_str)
    root.after(1000, atualiza_tempo)

def reiniciar_jogo():
    # Limpa todas as pilhas antes de distribuir as cartas novamente
    for pilha in [p1, p2, p3, p4, p5, p6, p7, p8, base_ouros, base_paus, base_copas, base_espadas]:
        pilha.clear()

    # Limpa todas as cartas selecionadas
    carta_selecionada.clear()
    start_game()

root = Tk()
root.title("Freecell - DCC")
root.geometry("1100x700")
root.configure(background="green")

restart_button = Button(root, text="Restart", command=reiniciar_jogo)
restart_button.place(x=450, y=20)

tempo_label = Label(root, text="Tempo: 00:00")
tempo_label.place(x=530, y=20)

# 8 montes
p1 = []
p2 = []
p3 = []
p4 = []
p5 = []
p6 = []
p7 = []
p8 = []

# 4 pilhas de base (uma para cada naipe)
base_ouros = []
base_paus = []
base_copas = []
base_espadas = []

class CardImage:
    def __init__(self, name, root, group):
        self.name = name
        self.group = group
        self.card_img = Image.open(f'cards/{name}.png')
        self.card_img_final = ImageTk.PhotoImage(self.card_img)
        self.bt = Button(root, image=self.card_img_final, command=lambda: selectedCard(
            self, self.name), borderwidth=0)

global carta_selecionada
carta_selecionada = []

def selectedCard(card_com, name_card):
    if (len(carta_selecionada) > 0):
        old_card = carta_selecionada.pop()
        old_card.bt.configure(highlightthickness=0)
        if (old_card != card_com):
            carta_selecionada.append(card_com)
            card_com.bt.configure(highlightthickness=4,
                                  highlightbackground="#37d3ff")
    else:
        carta_selecionada.append(card_com)
        card_com.bt.configure(highlightthickness=4,
                              highlightbackground="#37d3ff")

def start_game():
    global tempo_inicial
    tempo_inicial = time.time()
    atualiza_tempo()
    carta_selecionada.clear()
    for pilha in [p1, p2, p3, p4, p5, p6, p7, p8, base_ouros, base_paus, base_copas, base_espadas]:
        pilha.clear()
        
    naipes = ["ouros", "paus", "copas", "espadas"]
    valores = range(1, 14)

    deck = []

    for naipe in naipes:
        for v in valores:
            deck.append(f'{v}_of_{naipe}')

    for i in range(7):
        if (len(deck) > 0):
            card = random.choice(deck)
            deck.remove(card)
            p1.append(card)
        if (len(deck) > 0):
            card = random.choice(deck)
            deck.remove(card)
            p2.append(card)
        if (len(deck) > 0):
            card = random.choice(deck)
            deck.remove(card)
            p3.append(card)
        if (len(deck) > 0):
            card = random.choice(deck)
            deck.remove(card)
            p4.append(card)
        if (len(deck) > 0):
            card = random.choice(deck)
            deck.remove(card)
            p5.append(card)
        if (len(deck) > 0):
            card = random.choice(deck)
            deck.remove(card)
            p6.append(card)
        if (len(deck) > 0):
            card = random.choice(deck)
            deck.remove(card)
            p7.append(card)
        if (len(deck) > 0):
            card = random.choice(deck)
            deck.remove(card)
            p8.append(card)

    make_screen()

def frame_clicked(frame_name):
    if carta_selecionada:
        target_pile = frame_name.pilha
        move_card_to_pile(carta_selecionada[0].name, target_pile)
        carta_selecionada[0].bt.place(
            x=frame_name.winfo_x(), y=frame_name.winfo_y())
        carta_selecionada[0].bt.lift()
    else:
        print("nada selecionado!")
def move_card_to_pile(card, target_pile):
    if can_move_to_pile(card, target_pile):
        source_pile = next((p for p in [p1, p2, p3, p4, p5, p6, p7, p8] if card in p), None)
        source_base = next((p for p in [base_ouros, base_paus, base_copas, base_espadas] if card in p), None)
        
        if source_pile:
            source_pile.remove(card)
            target_pile.append(card)
        elif source_base:
            source_base.remove(card)
            target_pile.append(card)
        else:
            source_cell = carta_selecionada[0].group
            source_cell.remove(card)
            target_pile.append(card)
        
        if len(target_pile) == 13:
            for _ in range(13):
                target_pile.pop()
        
        update_gui()

def can_move_to_pile(card, pilha):
    if not pilha:
        return True

    top_card = pilha[-1]
    card_value, card_suit = card.split("_of_")
    top_value, top_suit = top_card.split("_of_")

    return int(card_value) == int(top_value) + 1 and card_suit == top_suit
def make_screen():
    pos_x = 30
    pos_y = 200
    fator_x = 125
    fator_y = 40

    for i in range(len(p1)):
        card_new = CardImage(p1[i], root, p1)
        card_new.bt.place(x=pos_x, y=pos_y+(fator_y*i))

    for i in range(len(p2)):
        card_new = CardImage(p2[i], root, p2)
        card_new.bt.place(x=pos_x+(fator_x*1), y=pos_y+(fator_y*i))

    for i in range(len(p3)):
        card_new = CardImage(p3[i], root, p3)
        card_new.bt.place(x=pos_x+(fator_x*2), y=pos_y+(fator_y*i))

    for i in range(len(p4)):
        card_new = CardImage(p4[i], root, p4)
        card_new.bt.place(x=pos_x+(fator_x*3), y=pos_y+(fator_y*i))

    for i in range(len(p5)):
        card_new = CardImage(p5[i], root, p5)
        card_new.bt.place(x=pos_x+(fator_x*4), y=pos_y+(fator_y*i))

    for i in range(len(p6)):
        card_new = CardImage(p6[i], root, p6)
        card_new.bt.place(x=pos_x+(fator_x*5), y=pos_y+(fator_y*i))

    for i in range(len(p7)):
        card_new = CardImage(p7[i], root, p7)
        card_new.bt.place(x=pos_x+(fator_x*6), y=pos_y+(fator_y*i))

    for i in range(len(p8)):
        card_new = CardImage(p8[i], root, p8)
        card_new.bt.place(x=pos_x+(fator_x*7), y=pos_y+(fator_y*i))

    ft_posX = 20
    ft_posX = 20
    ft_posY = 20
    ft_fator = 110
    frame1 = Frame(root, width=100, height=145, background="green",
                   highlightbackground="lightgreen", highlightthickness=2)
    frame1.bind("<Button-1>", lambda event: frame_clicked(frame1))
    frame1.place(x=ft_posX+(ft_fator*0), y=ft_posY)
    frame1.pilha = p1

    frame2 = Frame(root, width=100, height=145, background="green",
                   highlightbackground="lightgreen", highlightthickness=2)
    frame2.bind("<Button-1>", lambda event: frame_clicked(frame2))
    frame2.place(x=ft_posX+(ft_fator*1), y=ft_posY)
    frame2.pilha = p2

    frame3 = Frame(root, width=100, height=145, background="green",
                   highlightbackground="lightgreen", highlightthickness=2)
    frame3.bind("<Button-1>", lambda event: frame_clicked(frame3))
    frame3.place(x=ft_posX+(ft_fator*2), y=ft_posY)
    frame3.pilha = p3

    frame4 = Frame(root, width=100, height=145, background="green",
                   highlightbackground="lightgreen", highlightthickness=2)
    frame4.bind("<Button-1>", lambda event: frame_clicked(frame4))
    frame4.place(x=ft_posX+(ft_fator*3), y=ft_posY)
    frame4.pilha = p4

    ff_posX = 650
    ff_posY = 20
    ff_fator = 110
    frame5 = Frame(root, width=100, height=145, background="green",
                   highlightbackground="lightgray", highlightthickness=2)
    frame5.place(x=ff_posX+(ff_fator*0), y=ff_posY)
    frame5.pilha = base_ouros

    frame6 = Frame(root, width=100, height=145, background="green",
                   highlightbackground="lightgray", highlightthickness=2)
    frame6.place(x=ff_posX+(ff_fator*1), y=ff_posY)
    frame6.pilha = base_paus

    frame7 = Frame(root, width=100, height=145, background="green",
                   highlightbackground="lightgray", highlightthickness=2)
    frame7.place(x=ff_posX+(ff_fator*2), y=ff_posY)
    frame7.pilha = base_copas

    frame8 = Frame(root, width=100, height=145, background="green",
                   highlightbackground="lightgray", highlightthickness=2)
    frame8.place(x=ff_posX+(ff_fator*3), y=ff_posY)
    frame8.pilha = base_espadas

def update_gui():
    global frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8
    for i, frame in enumerate([frame5, frame6, frame7, frame8]):
        if len([base_ouros, base_paus, base_copas, base_espadas][i]) > 0:
            frame.configure(
                background="lightgray", highlightbackground="lightgray")
        else:
            frame.configure(background="green",
                            highlightbackground="lightgray")
    
    for frame, pilha in zip([frame1, frame2, frame3, frame4], [p1, p2, p3, p4]):
        if len(pilha) > 0:
            card = pilha[-1]
            card_img = Image.open(f'cards/{card}.png')
            card_img_final = ImageTk.PhotoImage(card_img)
            frame.configure(background="lightgreen",
                            highlightbackground="lightgreen")
            frame.card_img = card_img
            frame.card_img_final = card_img_final
            frame.bt.configure(image=card_img_final)
        else:
            frame.card_img = None
            frame.card_img_final = None
            frame.configure(background="green",
                            highlightbackground="lightgreen")
            frame.bt.configure(image="", state="normal")

if __name__ == "__main__":
    start_game()    
    root.mainloop()