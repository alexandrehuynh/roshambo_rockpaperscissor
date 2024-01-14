import random

def roshambo():
    
    choices = ["rock", "paper", "scissors"]
    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    print("Welcome to Roshambo!")
    print("exit, quit, stop, or leave at anytime \n")

    point_me, point_machines, stalemate = 0, 0, 0
    scoreboard = []

    while True: # start the lop
        user_input = input("Draw on scisssors...\n  Rock, Paper, Scissors\n\n    Shoot:").strip().lower()

        # break: allow user to leave game
        if user_input in ['exit', 'quit','forfeit', 'stop', 'surrender' 'leave', 'Exit', 'Quit', 'Forfeit', 'Stop', 'Surrender', 'Leave', 'e', 'q', 'f', 'l']:
            break

        if user_input not in choices: # edge case: valid user input
            print("Stop cheating. Only Rock, Paper, or Scissors\nReady? ")
            continue

        cpu_choice = random.choice(choices)
        print(f"CPU chose: {cpu_choice.capitalize()}")

        # Determine the winner
        if user_input == cpu_choice:
            result = "It's a tie! 🤝"
            stalemate += 1
        elif rules[user_input] == cpu_choice:
            result = "You win! 🏆"
            point_me += 1
        else:
            result = "You lose! 🤖"
            point_machines += 1

            
        # Print Recap
        print(f"\nRound Result: {result}")
        scoreboard.append((user_input, cpu_choice))
        print(f"Current Score: Team We - {point_me}, Machines - {point_machines}, Stalemates - {stalemate}\n")

    # Game Summary
    print("\nAtlas! The games have concluded! \n")
    print(f"Final Score: Team We - {point_me}, Machines - {point_machines}, Stalemate - {stalemate}")
    
    if point_me > point_machines:
        print("US HUMANS PREVAILED 👩‍🎓🧑‍💻🕵️‍♂️")
    
    elif point_me < point_machines:
        print("THE MACHINES HAVE WON 🤖🦾🦿")
    
    else:
        print("Words of the world wistfully weave a wayward, worrisome waltz 🌬🎑🗞")
    
    print('\n') # aesthetic touch 
    
    for index, (user, cpu) in enumerate(scoreboard, start=1):
        print(f"Round {index}: You chose {user.capitalize()}, CPU chose {cpu.capitalize()}")

# Main function
roshambo()
