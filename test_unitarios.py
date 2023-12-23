import unittest
from blackjack import play_game
from deck_class import Deck
from game_class import Game
from player_class import Player

class TestDealerHand(unittest.TestCase):# pragma: no cover

    def setUp(self):
        player1= Player()
        dealer=Player()
        game_deck=Deck()
        self.game = Game(player1,dealer,game_deck)

    def test_first_card_in_hand(self):
        # Setup the dealer's hand
        self.game.dealer.hand = [('Espadas', 'As', 1), ('Corazones', '2', 2)]
    
        # Test that the first card in the dealer's hand is 'Ace of Spades'
        self.assertEqual(self.game.dealer.hand[0], ('Espadas', 'As', 1))

    def test_sum_hand(self):
        self.game.dealer.hand = [('Espadas', 'As', 1), ('Corazones', '2', 2)]
        total= self.game.dealer.hand_total()
        self.assertEqual(total, 13)

    def test_draw_reset_draw(self):
        self.game.deck.shuffle()
        self.game.dealer.hand=self.game.deck.draw_card()
        card1=self.game.dealer.hand[0]
        self.game.dealer.reset_hand()
        self.game.deck.shuffle()
        self.game.dealer.hand=self.game.deck.draw_card()
        card2=self.game.dealer.hand[0]
        self.assertIsNot(card1, None)
        self.assertIsNot(card2, None)
        self.assertIsNotNone(card1)
        self.assertIsNotNone(card2)
        self.assertNotEqual(card1, card2)
    
    def test_checkWinner_PlayerWins(self):
        self.game.player.chips=100
        self.game.player.bet(20)

        self.game.bet_amount=20
        self.game.dealer.hand = [('Espadas', 'As', 1), ('Corazones', '2', 2)]
        self.game.player.hand=[('Espadas', 'Rey', 10), ('Corazones', 'Dama', 10)]

        self.game.check_winner()
        self.assertEqual(self.game.player.chips, 120)


    def test_checkWinner_DealerWins(self):
        self.game.player.chips=100
        self.game.player.bet(20)

        self.game.bet_amount=20
        self.game.dealer.hand = [('Espadas', 'Jack', 10), ('Corazones', 'As', 11)]
        self.game.player.hand=[('Espadas', 'Rey', 10), ('Corazones', 'Dama', 10)]

        self.game.check_winner()
        self.assertEqual(self.game.player.chips, 80)

    def test_checkWinner_Tie(self):
        self.game.player.chips=100
        self.game.player.bet(20)

        self.game.bet_amount=20
        self.game.dealer.hand = [('Espadas', 'Jack', 10), ('Picas', 'Dama', 10)]
        self.game.player.hand= [('Espadas', 'Rey', 10), ('Corazones', 'Dama', 10)]

        self.game.check_winner()
        self.assertEqual(self.game.player.chips, 100)

    def test_dealerTurn_Over17(self):
        self.game.dealer.hand = [('Espadas', 'Jack', 10), ('Picas', 'Dama', 10)]
        self.game.player.hand=[('Espadas', 'Rey', 10), ('Corazones', 'Dama', 10)]
        self.game.dealer_turn()
        cartas=len(self.game.dealer.hand)
        self.assertEqual(cartas, 2)
    
    def test_dealerTurn_Under7(self):
        self.game.dealer.hand = [('Espadas', 'Jack', 10), ('Picas', '3', 3)]
        self.game.player.hand=[('Espadas', 'Rey', 10), ('Corazones', '2', 2)]
        self.game.dealer_turn()
        cartas=len(self.game.dealer.hand)
        self.assertNotEqual(cartas, 2)

    def test_dealCards(self):
        self.game.deal_cards()
        cartas=len(self.game.dealer.hand)
        self.assertEqual(cartas, 2)

    def test_reciveBlackJack(self):
        self.game.dealer.hand = [('Espadas', 'Jack', 10), ('Picas', '3', 3)]
        self.game.player.chips=0
        self.game.player.hand=[('Espadas', 'Rey', 10), ('Corazones', 'As', 11)]
        self.game.bet_amount=100
        self.game.player_turn()
        total=self.game.player.hand_total()
        dinero=self.game.player.chips

        self.assertEqual(total, 21)
        self.assertEqual(dinero, 200)

    def test_printHand(self):
        self.game.dealer.hand = [('Espadas', 'Jack', 10), ('Picas', '3', 3)]
        self.game.player.hand=[('Espadas', 'Rey', 10), ('Corazones', 'As', 11)]

        mano=self.game.player.print_player_hand(1)

        self.assertTrue(len(mano),2)


if __name__ == '__main__':
    unittest.main()
