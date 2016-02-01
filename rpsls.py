# Rock-paper-scissors-lizard-Spock


# Modules
import random



# Helper methods
def name_to_number(name):
    # Converts rpsls throw to number
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Invalid throw: ", name



def number_to_name(number):
    # Converts number to a rpsls throw
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Invalid number: ", number



# Game logic
def rpsls(player_choice):
    """
    Rock-paper-scissors-lizard-Spock method.
    Prints player and winner rpsls object to the console,
    calls on two helper methods and uses control flow
    to compare choices, and prints result to the console.
    Computer choice is calculated with random module.
    """
    print

    print "Player chooses " + player_choice

    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0, 4)

    comp_choice = number_to_name(comp_number)

    print "Computer chooses " + comp_choice

    throw_outcome = (comp_number - player_number) % 5

    if throw_outcome == 0:
        print "Player and computer tie!"
    elif throw_outcome <= 2:
        print "Computer wins!"
    elif throw_outcome > 2:
        print "Player wins!"



# Driver Code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")