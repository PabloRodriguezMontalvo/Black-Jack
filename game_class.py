"""Gestiona la lógica del juego"""
from colorama import Fore

class Game:
    """Class Game. Recibe los jugadores que van a jugar y el mazo de cartas"""

    def __init__(self, player, dealer, deck):
        self.player = player
        self.dealer = dealer
        self.deck = deck
        self.deck.shuffle()
        self.bet_amount=0

    def deal_cards(self):
        """Reparte las cartas al jugador y al dealer"""
        for _ in range(2):
            self.player.add_card(self.deck.draw_card())
            self.dealer.add_card(self.deck.draw_card())
        print("Se están repartiendo las cartas")

    def place_bet(self):
        """Pregunta al jugador cuantas fichas quiere apostar """
        while True:
            try:
                bet=int(input(Fore.CYAN+"¿Cuantas fichas quieres apostar?: "))
                if self.player.bet(bet):
                    self.bet_amount=bet
                    break
            except ValueError:
                print("Apuesta incorrecta. Por favor introduzca un número")

    def player_turn(self):

        '''El jugador tendrá las opciónes pedir carta o plantarse.'''
        total=self.player.hand_total()
        print(Fore.RED+ f"Tu turno. Fichas ({self.player.chips})")
        self.player.print_player_hand(1)
        print(Fore.BLACK+ f"Total: {total}")
        print(Fore.YELLOW+
              "Mano Dealer:"+
               f"{self.dealer.hand[0][1]} de {self.player.hand[0][0]} y una carta oculta")
        if total==21:
            print(Fore.GREEN+"Blackjack! tu ganas.")
            print("\n\n")
            self.player.win_bet(self.bet_amount*2)
            return False

        while True:
            action= input(Fore.BLACK+"¿Quieres una carta más? [S/N]: ").lower()
            if action=='s':
                print("\n\n")
                card= self.deck.draw_card()
                self.player.add_card(card)
                total=self.player.hand_total()
                print(Fore.YELLOW+f"{card[1]} de {card[0]}. Total: {total}")
                if total>21:
                    print(Fore.GREEN+"Te pasaste, La banca gana")
                    print("\n\n")
                    return False
                if total==21:
                    print(Fore.GREEN+"Blackjack! tu ganas.")
                    print("\n\n")
                    self.player.win_bet(self.bet_amount*2)
                    return False

                self.player.print_player_hand(1)
                print(Fore.YELLOW+
                        "Mano Dealer: "+
                        f"{self.dealer.hand[0][1]} de {self.player.hand[0][0]}"
                        +"y una carta oculta")


            elif action=='n':
                total=self.player.hand_total()
                print (Fore.RED+f"Te plantaste con un valor de cartas de {total}")
                print("\n\n")
                return True
            else:
                print("Por favor, elija S o N para seguir")

    def dealer_turn(self):
        """El Dealer recibirá cartas hasta que tenga 17 o más """
        while True:
            self.dealer.print_player_hand(0)
            total=self.dealer.hand_total()
            if total<17:
                card= self.deck.draw_card()
                self.dealer.add_card(card)
                print(f"{card[1]} de {card[0]}. Total: {total}")
            else:
                print(f"El dealer se planta con {total}")
                return total

    def check_winner(self):
        """Comprueba quien es el ganador """
        player_total=self.player.hand_total()
        dealer_total=self.dealer.hand_total()

        if dealer_total>21:
            print(Fore.GREEN+"La banca se ha pasado, ¡tu ganas!")
            self.player.win_bet(self.bet_amount*2)
        elif player_total>dealer_total:
            print(Fore.GREEN+f"{player_total} > {dealer_total} ¡tu ganas!")
            self.player.win_bet(self.bet_amount)
        elif player_total<dealer_total:
            print(Fore.GREEN+f"{player_total} < {dealer_total} ¡Dealer gana!")
        else:
            print(Fore.GREEN+f"{player_total} = {dealer_total} ¡Empate!")
            self.player.win_bet(self.bet_amount)

    def play_game(self):
        """Iniciador del juego"""
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.place_bet()
        self.deal_cards()
        if self.player_turn():
            #Si el jugador no se ha pasado ni ha conseguido blackjack, jugaría la maquina
            self.dealer_turn()
            self.check_winner()
