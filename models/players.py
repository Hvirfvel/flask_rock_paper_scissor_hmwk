def compare_hands(player_1, player_2):
        if player_1.hand == player_2.hand:
            return None
        elif player_1.hand == "rock":
            if player_2.hand == "paper":
                return player_2
            elif player_2.hand == "scissors":
                return player_1
        elif player_1.hand == "paper":
            if player_2.hand == "rock":
                return player_1
            elif player_2.hand == "scissors":
                return player_2
        elif player_1.hand == "scissors":
            if player_2.hand == "rock":
                return player_2
            elif player_2.hand == "paper":
                return player_1