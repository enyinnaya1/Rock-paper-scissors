import random

print("""This is a rock paper scissors Game.
Enter any of the following options:
R for rock
P for paper
and S for scissors""")

# list of game options
options = ["R", "P", "S"]

# loop for iteration of the program
while True:
    PSln = input("rock paper scissors!.. enter your choice: ")  # takes user input
    if PSln in options:
        CPU = random.choice(options)    # checks if user selection is valid

        # Evaluation of CPU and players selections to declare the winner if the game
        if PSln == CPU:
            print("Player(" + PSln + ") : CPU(" + CPU + ")")
            print("Tie!")
            continue

        elif (CPU == options[0]) and (PSln == options[1]):
            print("Player(paper):CPU(rock)")
            print("""paper covers rock!
            Player wins!""")
            break

        elif (CPU == options[0]) and (PSln == options[2]):
            print("Player(scissors):CPU(rock)")
            print("""rock crushes scissors!
            CPU wins!""")
            break

        elif (CPU == options[2]) and (PSln == options[1]):
            print("Player(paper):CPU(scissors)")
            print("""scissors cuts paper!
            CPU wins!""")
            break

        elif (CPU == options[2]) and (PSln == options[0]):
            print("Player(rock):CPU(scissors)")
            print("""rock crushes scissors!
            Player wins!""")
            break

        elif (CPU == options[1]) and (PSln == options[2]):
            print("Player(scissors):CPU(paper)")
            print("""scissors cuts paper!
            Player wins!""")
            break

        else:
            print("Player(rock):CPU(paper)")
            print("""paper covers rock!
            CPU wins!""")
            break

    else:
        print("you have selected an invalid option")
        continue    # reiterates the program if the player selection is invalid
