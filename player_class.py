"""Gestiona la funcionalidad de los jugadores,
un jugador tiene una mano de cartas y puede robar más"""
import random
from colorama import Fore

class Player:
    """Represents a player in a card game."""

    def __init__(self):
        self.hand = []
        self.chips = 100

    def bet(self, amount):
        """Crea una apuesta, si el jugador no tiene suficientes fichas, 
        la apuesta no se realizará"""
        if amount>self.chips:
            print("No tienes suficientes fichas para apostar esa cantidad")
            return False
        self.chips-=amount
        print(f"Has apostado {amount} fichas")
        return True

    def hand_total(self):
        """ Devuelve el valor total de la mano actual de la ronda del jugador """
        total=0
        aces=0
        for card in self.hand:
            if card[1]=='As':
                aces+=1
                total+=11
            else:
                total+=card[2]

        while total >21 and aces>0:
            total -=10
            aces -=1

        return total

    def print_player_hand(self, jugador):
        """Formatea y enseña la mano del jugador """
        array_cards=[f"{card[1]} de {card[0]}" for card in self.hand]
        hand_player= ", ".join(array_cards)
        if jugador==1:
            print(Fore.BLUE+ f"Mano: {hand_player}")
        else:
            print(Fore.RED+ f"Mano: {hand_player}")
        return array_cards


    def win_bet(self, amount):
        """Añade las ganancias de la apuesta ganada al monedero del jugador """
        self.chips+=amount
        print(f"Has ganado {amount} fichas")

    def add_card(self, card):
        """Añade una carta a la mano"""
        self.hand.append(card)

    def reset_hand(self):
        """Reiniciamos la mano para cada ronda"""
        self.hand = []
    def shuffle(self):
        """Baraja la mano"""
        random.shuffle(self.hand)
