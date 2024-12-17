'''
A "big 6" bet pays even money if a 6 is rolled before a 7. Assuming 30 $5 bets 
per hour, write a Monte Carlo simulation that estimates the cost per hour and 
the standard deviation of that cost of playing "big 6" bets.
'''

import random
import numpy as np


def roll_die():
    return random.choice([1, 2, 3, 4, 5, 6])


# game class

class game(object):
    def __init__(self):
        self.wins, self.losses = 0, 0
        
    def play_hand(self):
        throw = roll_die() + roll_die()
        if throw == 7:
            self.losses += 1
        elif throw == 6:
            self.wins += 1
        else:
            while True:
                throw = roll_die() + roll_die()
                if throw == 7:
                    self.losses += 1
                    break
                elif throw == 6:
                    self.wins += 1
                    break
                
    def results(self):
        return (self.wins, self.losses)
    

# Simulating the game

def game_sim(hands_per_game, num_games):
    """Assumes hands_per_game and num_games are ints > 0
    Play num_games games of hands_per_game hands; print results"""
    games = []
    
    # Play num_games games
    for t in range(num_games):
        g = game()
        for i in range(hands_per_game):
            g.play_hand()
        games.append(g)
        
    # Produce statistics for each game
    hourly_cost_per_game = []
    for g in games:
        wins, losses = g.results()
        hourly_cost_per_game.append((losses - wins) * 5)
        
    # Produce and print summary statistics
    mean_hourly_cost = "$" + str(round((sum(hourly_cost_per_game) / num_games), 2))
    sigma_hourly_cost = "$" + str(round(np.std(hourly_cost_per_game), 2))
    print("Mean cost per hour =", mean_hourly_cost, ";", "Standard deviation of the cost =", sigma_hourly_cost)


game_sim(30, 1000000)
