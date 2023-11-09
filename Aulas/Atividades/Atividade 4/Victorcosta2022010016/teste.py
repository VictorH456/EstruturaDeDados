from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title("Freecell - DCC")
root.geometry("1100x700")
root.configure(background="green")

# Lista de pilhas para as cartas
piles = [[] for _ in range(8)]

tableaus = [[] for _ in range(8)]
free_cells = [None] * 4
foundation = [[] for _ in range(4)]

class CardImage:
    def __init__(self, name, root, pile):
        self.name = name
        self.pile = pile
        self.card_img = Image.open(f'cards/{name}.png')
        self.card_img_final = ImageTk.PhotoImage(self.card_img)
        self.bt = Button(root, image=self.card_img_final, command=lambda: selectedCard(self), borderwidth=0)

global carta_selecionada
carta_selecionada = None

def selectedCard(card):
    global carta_selecionada
    if not carta_selecionada:
        carta_selecionada = card
        card.bt.configure(highlightthickness=4, highlightbackground="#37d3ff")
    else:
        if move_card(carta_selecionada, card):
            carta_selecionada.bt.place(x=carta_selecionada.bt.winfo_x(), y=carta_selecionada.bt.winfo_y())
            carta_selecionada.pile.remove(carta_selecionada.name)
            card.pile.append(carta_selecionada.name)
            carta_selecionada = None
            make_screen()
        else:
            carta_selecionada.bt.configure(highlightthickness=0)
            carta_selecionada = card
            card.bt.configure(highlightthickness=4, highlightbackground="#37d3ff")

def start_game():
    global carta_selecionada
    carta_selecionada = None

    # Limpar as pilhas atuais
    for pile in piles:
        pile.clear()

    # Criar baralho
    naipes = ["ouros", "paus", "copas", "espadas"]
    valores = range(1, 14)

    deck = []

    for naipe in naipes:
        for v in valores:
            deck.append(f'{v}_of_{naipe}')

    # Distribuir as cartas entre 8 pilhas
    for pile in piles:
        for _ in range(6):
            if len(deck) > 0:
                card = random.choice(deck)
                deck.remove(card)
                pile.append(card)

    make_screen()

def restart_game():
    start_game()

def move_card(source_card, dest_card):
    source_rank, source_suit = source_card.name.split("_of_")
    dest_rank, dest_suit = dest_card.name.split("_of_")
    rank_values = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12, '13': 13}

    if source_suit != dest_suit and rank_values[source_rank] == rank_values[dest_rank] - 1:
        return True
    return False

def frame_clicked(frame_name):
    if carta_selecionada:
        print(carta_selecionada.name)
        print(frame_name.winfo_name())

        carta_selecionada.bt.place(
            x=frame_name.winfo_x(), y=frame_name.winfo_y())
        carta_selecionada.bt.lift()

    else:
        print("nada selecionado!")

def make_screen():
    for widget in root.winfo_children():
        if widget != restart_button:
            widget.destroy()

    # Cria cartas como botões e coloca na tela

    pos_x = 30
    pos_y = 200
    fator_x = 125
    fator_y = 40

    for i, pile in enumerate(piles):
        for j, card_name in enumerate(pile):
            card_new = CardImage(card_name, root, pile)
            card_new.bt.place(x=pos_x + (fator_x * i), y=pos_y + (fator_y * j))

    # -------------------------------------------  FRAMES
    # Cria Frames de Troca
    ft_posX = 20
    ft_posY = 20
    ft_fator = 110

    for i, frame in enumerate(free_cells):
        frame_widget = Frame(root, width=100, height=145, background="green", highlightbackground="lightgreen", highlightthickness=2)
        frame_widget.bind("<Button-1>", lambda event, f=frame: frame_clicked(f))
        frame_widget.place(x=ft_posX + (ft_fator * i), y=ft_posY)

    # Cria Frames Finais
    ff_posX = 650
    ff_posY = 20
    ff_fator = 110

    for i, frame in enumerate(foundation):
        frame_widget = Frame(root, width=100, height=145, background="green", highlightbackground="lightgray", highlightthickness=2)
        frame_widget.place(x=ff_posX + (ff_fator * i), y=ff_posY)

start_game()

# Botão de Restart
restart_button = Button(root, text="Restart Game", command=restart_game)
restart_button.pack()

root.mainloop()