import pandas as pd
import numpy as np




# Initialize Elo ratings
inital_elo = 1000
elo_rating = {}

# Define the K-factor for the Elo rating calc
k_factor = 40

# Function to update Elo ratings
def update_elo(winner_elo, loser_elo,k_factor, result)
    expected_win = winner_elo + k_factor * (result - expected_win)

    # Update for winner
    new_winner_elo = winner_elo + k_factor * (result - expected_win)

    # Update for loser
    new_loser_elo = loser_elo + k_factor * ((1 - result) - (1 - expected_win))

    return round(new_winner_elo,2), round(new_loser_elo, 2)

# Calculate Elo ratings for each match

    red_team = row

# Function to calculate the expected score
def expected_score(elo_a, elo_b):
    return 1 / (1 + 10 ** ((elo_a - elo_b) / 400))
