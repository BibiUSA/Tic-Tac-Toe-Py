"""Create a tic-tac-toe game."""
from random import random
import time


def main():

    """Hold value within a box"""
    moves = {"A1": " ",
             "A2": " ",
             "A3": " ",
             "B1": " ",
             "B2": " ",
             "B3": " ",
             "C1": " ",
             "C2": " ",
             "C3": " "
             }

    """Combinations required to win."""
    winning_combinations = [
        ["A1", "A2", "A3"],
        ["B1", "B2", "B3"],
        ["C1", "C2", "C3"],
        ["A1", "B1", "C1"],
        ["A2", "B2", "C2"],
        ["A3", "B3", "C3"],
        ["A1", "B2", "C3"],
        ["A3", "B2", "C1"]
    ]

    """Used to keep all the choices made."""
    user_selections = []
    computer_selections = []

    """Choices that are left."""
    choice_left = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

    def play_box():
        """Print out the box with values."""
        row_a = "  A     B    C"
        row_b = f"1  {moves['A1']} | {moves['B1']}  | {moves['C1']}  "
        row_c = " ----|----|----"
        row_d = f"2  {moves['A2']} | {moves['B2']}  | {moves['C2']}  "
        row_e = " ----|----|----"
        row_f = f"3  {moves['A3']} | {moves['B3']}  | {moves['C3']}  "
        row_g = "     |    |    "

        print(row_a)
        print(row_b)
        print(row_c)
        print(row_d)
        print(row_e)
        print(row_f)
        print(row_g)

    print("Welcome to the game of tic tac toe!")

    def coin_toss():
        """Ask user for heads or tails."""
        while True:
            coin_choice = input("To figure out who goes first, choose "
                                "heads or tails. \n").upper()
            choices_head = ["HEAD", "HEADS", "H"]
            choices_tails = ["TAILS", "TAIL", "T"]
            if coin_choice in choices_head:
                return "heads"
            elif coin_choice in choices_tails:
                return "tails"

    answer = coin_toss()
    print(f"You chose {answer}.")

    def coin():
        """Generate random head or tails answer"""
        if random() < 0.50:
            return "heads"
        else:
            return "tails"

    coin_flip_result = coin()

    time.sleep(1)
    print(f"Coin flip result: ")
    time.sleep(1)
    print(coin_flip_result)

    time.sleep(1)

    if answer == coin_flip_result:
        """Assign sign to user and gives computer chance to move."""
        print(f"Since you chose {answer}, you go first.")
        user_sign = "X"
        computer_sign = "O"
    else:
        print("Computer won the coin toss. Computer goes first.")
        user_sign = "O"
        computer_sign = "X"
        next_move_chance = round(random()*4)
        print(next_move_chance)
        next_options = ["A1", "C1", "A3", "C3", "B2"]
        next_move = next_options[next_move_chance]
        moves[next_move] = computer_sign
        choice_left.remove(next_move)
        computer_selections.append(next_move)

    def block(selections, sign):
        """Figure out what box should be blocked. Used to prevent
        opponent winning"""
        for item in winning_combinations:
            result = 0
            if moves[item[0]] != sign and moves[item[1]] != sign and \
                    moves[item[2]] != sign:
                for x in item:
                    for i in selections:
                        if x == i:
                            result += 1
            if result == 2:
                for each in item:
                    new_result = 0
                    for i in selections:
                        if each == i:
                            new_result += 1
                    if new_result == 0:
                        return each

    def win(sign):
        """Choose own selection to see if you won. Opposing sign."""
        for item in winning_combinations:
            if moves[item[0]] == sign and moves[item[1]] == sign and \
                    moves[item[2]] == sign:
                return "winner"

    play_box()

    def user_turn():
        """Ask user for input and plays the input."""
        while True:
            print("Choices left:", choice_left)
            answers = input("Choose the box you want to play:")\
                .capitalize()
            if answers in choice_left:
                moves[answers] = user_sign
                choice_left.remove(answers)
                user_selections.append(answers)
                break
            else:
                print("Selection not valid."
                      "Choose a choice from the choices left.")
                play_box()

    user_turn()

    play_box()
    print(choice_left)

    time.sleep(1)
    print("Computers turn...")

    if moves["B2"] == " ":
        """Take center spot if available or else take a corner spot."""
        moves["B2"] = computer_sign
        computer_selections.append("B2")
        choice_left.remove("B2")
    else:
        while True:
            """Take one of the corner spot."""
            next_move = ["A1", "A3", "C1", "C3"]
            next_move_chance = round(random()*3)
            choice = next_move[next_move_chance]
            if moves[choice] == " ":
                moves[choice] = computer_sign
                choice_left.remove(choice)
                computer_selections.append(choice)
                break

    play_box()
    user_turn()
    play_box()
    print(choice_left)

    def next_move():
        """Figure out next move for the computer."""
        if random() > 0.9:
            print("option 1 ran")
            next_move_chances = round(random() * len(choice_left)-1)
            choices = choice_left[next_move_chances]
            moves[choices] = computer_sign
            choice_left.remove(choices)
            computer_selections.append(choices)
        else:
            print("we need to work it out")
            next_choice = block(computer_selections, user_sign)
            print("Next Choice", next_choice)
            if next_choice is not None:
                moves[next_choice] = computer_sign
                choice_left.remove(next_choice)
                computer_selections.append(next_choice)
            else:
                best_choice = block(user_selections, computer_sign)
                print("Defend Move", best_choice)
                if best_choice is not None:
                    moves[best_choice] = computer_sign
                    choice_left .remove(best_choice)
                    computer_selections.append(best_choice)
                else:
                    print("final option ran")
                    next_move_prob = round(
                        random() * len(choice_left) - 1)
                    choice_now = choice_left[next_move_prob]
                    moves[choice] = computer_sign
                    choice_left.remove(choice_now)
                    computer_selections.append(choice_now)

    next_move()
    print(choice_left)
    play_box()
    user_turn()

    play_box()
    win_result = win(user_sign)
    if win_result == "winner":
        print("You won!!")
        exit()

    next_move()
    print(choice_left)
    play_box()
    win_result = win(computer_sign)
    if win_result == "winner":
        print("Computer won!!")
        exit()

    user_turn()

    play_box()
    win_result = win(user_sign)
    if win_result == "winner":
        print("You won!!")
        exit()

    print(choice_left)

    next_move()
    print(choice_left)
    play_box()
    win_result = win(computer_sign)
    if win_result == "winner":
        print("Computer won!!")
        exit()

    if len(choice_left) == 0:
        print("Draw")
        exit()

    user_turn()
    play_box()
    win_result = win(user_sign)
    if win_result == "winner":
        print("You won!!")
        exit()

    if len(choice_left) == 0:
        print("Draw")
        exit()


main()
