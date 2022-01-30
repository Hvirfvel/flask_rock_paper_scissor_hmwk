class Player():

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def compare_hands(self, player_1, player_2):
        if player_1.hand == player_2.hand:
            return None
        elif player_1.hand == "rock":
            if player_2.hand == "paper":
                return player_2.name
            elif player_2.hand == "scissors":
                return player_1.name
        elif player_1.hand == "paper":
            if player_2.hand == "rock":
                return player_1.name
            elif player_2.hand == "scissors":
                return player_2.name
        elif player_1.hand == "scissors":
            if player_2.hand == "rock":
                return player_2.name
            elif player_2.hand == "paper":
                return player_1.name
        

    