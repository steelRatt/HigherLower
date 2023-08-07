# Higher or Lower

import random
import game_data


def initialise_data():
    """Initialises data for the start of a new game"""
    return game_data.data


def get_random_data(data_list):
    """Selects a random entry from the list and then removes it"""
    data1 = random.choice(data_list)
    data_list.remove(data1)
    return data1


def check_guess(guess, follower_count1, follower_count2):
    """Checks if the guessed account has more followers"""
    if guess == "A":
        if follower_count1 > follower_count2:
            return True
        else:
            return False
    else:
        if follower_count1 > follower_count2:
            return False
        else:
            return True


def play(all_data):
    """The main game"""
    # Assign data
    data1 = get_random_data(all_data)
    data2 = get_random_data(all_data)

    # Comparison
    print(f"Compare A: {data1['name']} || {data1['description']} || {data1['country']}\n\nVs.\n")
    print(f"Against B: {data2['name']} || {data2['description']} || {data2['country']}")

    # Get user's guess
    guess = input("Who has more followers? (A/B): ")

    # Check if guess is correct
    return check_guess(guess, data1['follower_count'], data2['follower_count'])


def game_loop():
    """Allows the game to play again"""
    # Refresh the list for start of a new game
    data = initialise_data()

    is_right = True
    score = 0

    while is_right:
        is_right = play(data)

        if is_right:
            score += 1
            print(f"You're right! Current score: {score}")

    print(f"You lose! Final score: {score}")


game_loop()


# Two Instagram accounts are chosen from game_data, A and B
# User has to guess which one has more followers
# If they get it right, score is increased by 1
# User then has to compare B against C and guess which has more followers
# This continues until all have been guessed or they lose
# If they guess incorrectly, game is over and score is displayed
