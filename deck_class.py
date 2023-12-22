"""Gestiona la funcionalidad del mazo de cartas, se puede barajar el mazo y robar una carta"""

import random

class Deck:
    """Handle the Deck to War Game"""

    def __init__(self):
        self.suits = ['Espadas', 'Corazones', 'Diamantes', 'Picas']
        self.values = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Dama', 'Rey']
        self.card_values = {'As': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                            '9': 9, '10': 10, 'Jack': 10, 'Dama': 10, 'Rey': 10}
        self.deck = []

        for suit in self.suits:
            for value in self.values:
                self.deck.append((suit, value, self.card_values[value]))

    def shuffle(self):
        """Shuffle all the cards inside on the deck"""
        print("Barajando el mazo")
        random.shuffle(self.deck)

    def draw_card(self):
        """Draw a card from top and remove it from the deck"""
        if len(self.deck) == 0:
            return None
        return self.deck.pop()
