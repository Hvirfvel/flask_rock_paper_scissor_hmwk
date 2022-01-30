import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Player 1", "rock")

    def test_both_players_have_rock__returns_draw(self):
        player_2 = Player("Player 2", "rock")
        self.assertEqual(None, self.player.compare_hands(self.player, player_2))
    
    def test_both_players_have_paper__returns_draw(self):
        player_1 = Player("Player 1", "paper")
        player_2 = Player("Player 2", "paper")
        self.assertEqual(None, self.player.compare_hands(player_1, player_2))
    
    def test_both_players_have_scissors__returns_draw(self):
        player_1 = Player("Player 1", "scissors")
        player_2 = Player("Player 2", "scissors")
        self.assertEqual(None, self.player.compare_hands(player_1, player_2))

    def test_player_1_has_rock_player_2_has_paper__returns_player_2(self):
        player_2 = Player("Player 2", "paper")
        self.assertEqual("Player 2", self.player.compare_hands(self.player, player_2))

    def test_player_1_has_rock_player_2_has_scissors__returns_player_1(self):
        player_2 = Player("Player 2", "scissors")
        self.assertEqual("Player 1", self.player.compare_hands(self.player, player_2))

    def test_player_1_has_paper_player_2_has_rock__returns_player_1(self):
        player_1 = Player("Player 1", "paper")
        player_2 = Player("Player 2", "rock")
        self.assertEqual("Player 1", self.player.compare_hands(player_1, player_2))

    def test_player_1_has_paper_player_2_has_scissors__returns_player_2(self):
        player_1 = Player("Player 1", "paper")
        player_2 = Player("Player 2", "scissors")
        self.assertEqual("Player 2", self.player.compare_hands(player_1, player_2))
    
    def test_player_1_has_scissors_player_2_has_rock__returns_player_2(self):
        player_1 = Player("Player 1", "scissors")
        player_2 = Player("Player 2", "rock")
        self.assertEqual("Player 2", self.player.compare_hands(player_1, player_2))
    
    def test_player_1_has_scissors_player_2_has_paper__returns_player_1(self):
        player_1 = Player("Player 1", "scissors")
        player_2 = Player("Player 2", "paper")
        self.assertEqual("Player 1", self.player.compare_hands(player_1, player_2))
    
    