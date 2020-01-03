import random
import json

with open("rock_paper_scissors_json.json", "r") as myfile:
    data = myfile.read()

game_data = json.loads(data)
player_choice = None
pick_list = []
strengths = []

for item in game_data:
    pick_name = item["name"]
    pick_list.append(pick_name)

wins = {"player": 0, "computer": 0}
validate_player_counter = 0


def validate_player(input):
    global validate_player_counter
    if input not in pick_list:
        validate_player_counter += 1
        print("Try again, pick between:" + str(pick_list).strip("[]") + "\n")
        if validate_player_counter == 3:
            print("Seems like the game instructions are unclear.")
            print("Closing the game due to incompetence.")
            exit()
        ask_player("again")


def ask_player(*args):
    global player_choice
    if args == "again":
        player_choice = input().lower()
    else:
        player_choice = input(
            "Choose between " + str(pick_list).strip("[]") + "\n"
        ).lower()

    validate_player(player_choice)
    return player_choice


def ask_computer():
    choice = random.choice(pick_list)

    return choice


def score(name):
    global wins
    wins[name] = wins[name] + 1
    if wins[name] <= 2:
        print(name.capitalize() + " has won this round.\n")
        play()
    else:
        print(name.capitalize() + " has won the game.\n")
        exit()


def fetch_strenght(player_choice):
    global strengths
    for strengths_list in game_data:
        if strengths_list["name"] == player_choice:
            strengths = strengths_list["strength"]

    return strengths


def play():
    global player_choice
    ask_player()
    computer_choice = ask_computer()
    print(
        "The player picked "
        + player_choice
        + " and the computer picked "
        + computer_choice
        + ".\n"
    )

    if player_choice == computer_choice:
        print("The game is a tie.\n")
        play()

    else:
        fetch_strenght(player_choice)
        if computer_choice in strengths:
            score("player")
        else:
            score("computer")


print("Best out of three!")
play()
