from flask import render_template
from app import app
from models.player import *
from models.players import compare_hands

@app.route('/')
def index():
    return "Hello World"

@app.route('/<player_1_hand>/<player_2_hand>')
def result(player_1_hand, player_2_hand):
    print("It works")
    player_1 = Player("Player 1", player_1_hand)
    player_2 = Player("Player 2", player_2_hand)
    winner = compare_hands(player_1, player_2)
    return render_template('index.html', title='Rock, paper, scissors', winner=winner)