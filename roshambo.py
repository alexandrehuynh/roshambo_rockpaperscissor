import random

def roshambo():
    
    # define variables
    choices = ["rock", "paper", "scissors"]
    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    # display screen
    print("Welcome to Roshambo!")
    print("exit, quit, stop, or leave at anytime \n")

    # set scoreboard
    point_me, point_machines, stalemate = 0, 0, 0
    scoreboard = []

    while True: # start game of roshambo
        user_input = input("Draw on scisssors...\n  Rock, Paper, Scissors\n\n    Shoot:").strip().lower()

        # break: allow user to leave game
        if user_input in ['exit', 'quit','forfeit', 'stop', 'surrender' 'leave', 'Exit', 'Quit', 'Forfeit', 'Stop', 'Surrender', 'Leave', 'e', 'q', 'f', 'l']:
            break

        if user_input not in choices: # edge case: valid user input
            print("Stop cheating. Only Rock, Paper, or Scissors\nReady? ")
            continue

        # cpu's move
        cpu_choice = random.choice(choices)
        print(f"CPU chose: {cpu_choice.capitalize()}")

        # who's the winner
        if user_input == cpu_choice:
            result = "It's a tie! 🤝"
            stalemate += 1
        elif rules[user_input] == cpu_choice:
            result = "You win! 🏆"
            point_me += 1
        else:
            result = "You lose! 🤖"
            point_machines += 1

            
        # round recap, update scoreboard
        print(f"\nRound Result: {result}")
        scoreboard.append((user_input, cpu_choice))
        print(f"Current Score: Team We - {point_me}, Machines - {point_machines}, Stalemates - {stalemate}\n")

    # game over, show final score and winner
    print("\nAtlas! The Games have Concluded! \n")
    print(f"Final Score: Team We - {point_me}, Machines - {point_machines}, Stalemate - {stalemate}")
    
    if point_me > point_machines:
        print("US HUMANS PREVAILED 👩‍🎓🧑‍💻🕵️‍♂️")
    
    elif point_me < point_machines:
        print("THE MACHINES HAVE WON 🤖🦾🦿")
    
    else:
        print("Words of the world wistfully weave a wayward, worrisome waltz 🌬🎑🗞")
    
    print('\n') 
    
    # display recap of all the rounds
    print(f"Round Recaps: ")
    for index, (user, cpu) in enumerate(scoreboard, start=1):
        print(f"Round {index}: You chose {user.capitalize()}, CPU chose {cpu.capitalize()}")

####    Main function    ####
roshambo()
