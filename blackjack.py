"""Initiate the Black Jack Game """
from colorama import Fore

import deck_class
import player_class
import game_class

def play_game():
    """Star the Game """

    player1= player_class.Player()
    dealer=player_class.Player()
    game_deck=deck_class.Deck()
    my_game= game_class.Game(player1,dealer,game_deck)
    while True:
        my_game.play_game()
        if player1.chips<=0:
            print("TE QUEDASTE SIN MONEDAS, FIN DEL JUEGO")
            break
        play_again= input(Fore.WHITE+"¿Quieres jugar de nuevo?: [S/N]: ").lower()
        if play_again== 'n':
            break

if __name__ =="__main__":
    play_game()
