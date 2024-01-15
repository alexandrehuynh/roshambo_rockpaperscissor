import random

def roshambo():
    
    # define variables
    choices = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    choice_keys = {"r": "rock", "p": "paper", "s": "scissors"}
    exit_commands = {'exit', 'end', 'forfeit', 'leave', 'quit', 'stop', 'surrender', 'e', 'l', 'f', 'q'}
    tie_emoji, win_emoji, lose_emoji = "🤝", "🏆", "🤖"
    
    # display screen
    print("Welcome to Roshambo!")
    print("Type 'exit', 'forfeit', quit', 'stop', 'surrender' or 'leave' at any time to stop the game.\n")
    
    # set scoreboard
    scores = {"Player": 0, "CPU": 0, "Stalemate": 0}
    scoreboard = []

    while True: # start game of roshambo
        user_input = input("Draw on shoot...\n  Rock, Paper, Scissors\n\n    Shoot:").strip().lower()

        # break: allow user to leave game
        if user_input in exit_commands:
            break
        
        user_choice = choice_keys.get(user_input, user_input)
            
        if user_choice not in choices: # edge case: valid user input
            print("Stop cheating. Only Rock, Paper, or Scissors\nReady? ")
            continue

        # cpu's move
        cpu_choice = random.choice(list(choices.keys()))
        print(f"CPU chose: {cpu_choice.capitalize()}\n")
        
        # who's the winner
        if user_choice == cpu_choice:
            result, winner = "It's a tie! " + tie_emoji, "Stalemate"
        
        elif choices[user_choice] == cpu_choice:
            result, winner = "You win! " + win_emoji, "Player"
        
        else:
            result, winner = "You lose! "+ lose_emoji, "CPU"
            
        # round recap, update scoreboard
        print(f"\nRound Result: {result}")
        scores[winner] += 1
        scoreboard.append((user_choice, cpu_choice))
        print(f"{result}\nCurrent Score: {scores}\n")
        
    # game over, show final score and winner
    print("\nAtlas! The Games have Concluded! \n", scores)
    print("\nFinal Score:", scores)
           
    if scores["Player"] > scores["CPU"]:
        print("Humans Prevail! 👩‍🎓🧑‍💻🕵️‍♂️")
    
    elif scores["Player"] < scores["CPU"]:
        print("The Machines Win! 🤖🦾🦿")
    
    else:
        print("Words of the world wistfully weave a wayward, worrisome waltz with a Stalemate between Humans and Machines! 🌬🎑🗞")


    # display recap of all the rounds
    print(f"\nRound Recaps: ")
    for index, (player, cpu) in enumerate(scoreboard, start=1):
        print(f"Round {index}: You chose {player.capitalize()}, CPU chose {cpu.capitalize()}")

####    Main function    ####
roshambo()
