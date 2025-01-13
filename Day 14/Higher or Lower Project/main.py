from game_data import data
from art import logo, vs
import random


def prompt_compares():
    score = 0
    playing = True
    while playing:
        random_a = random.choice(data)
        print(random_a['name'],random_a['description'],random_a['country'])

        print(vs)

        random_b = random.choice(data)
        print(random_b['name'],random_b['description'],random_b['country'])
        user_choice = input(f"Who has more followers  {random_a['name']} or {random_b['name']} Choose A or B?: ").lower()
        if user_choice == "a" and random_a['follower_count'] > random_b['follower_count']:
            score += 1
            random_b = random_a
            print("nice keep going")
            print(score)
        elif user_choice == "a" and random_a['follower_count'] < random_b['follower_count']:
            score += 0
            print(score)
            print("Sorry You got it wrong buddy better luck next time")
            playing = False

        elif user_choice == "b" and random_b['follower_count'] > random_a['follower_count']:
            score += 1
            print("nice keep going")
            print(score)

        elif user_choice == "b" and random_b['follower_count'] < random_a['follower_count']:
            score += 0
            print(score)
            print("Sorry You got it wrong buddy better luck next time")
            playing = False



prompt_compares()