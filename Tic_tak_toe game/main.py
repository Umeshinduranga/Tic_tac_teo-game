#add module part

import time
import os
import webbrowser
from sub.functions import game_interface, inspect_win, make_move, save_session, load_session, print_scoreboard, print_menu, single_game


#game main loop
def main():
    print("\nWelcome to tic tac toe game!")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            #gamer 1
            print("\nPlayer 1")
            gamer1 = input("Enter your name: ")

            #gamer 2
            print("\nPlayer 2")
            gamer2 = input("Enter your name: ")
            print("\n")
            
            score_board = {gamer1: 0, gamer2: 0}  
            currunt_player = gamer1
            player_choice = {'X': "", 'O': ""}
            options = ['X', 'O']

            #start game with 0.9 delay
            print("Starting the game in...")
            for i in range(3, 0, -1):
                print(i)
                time.sleep(0.9)

            while True:
                
                print(f"\nTurn to choose for {currunt_player}")
                print("\nEnter 1 for X")
                print("Enter 2 for O")
                print("Enter 3 to Quit")
            
                try:
                    player_option = int(input())
                    
                except ValueError:
                    print("Invalid input. Try again.")
                    continue

                if player_option == 1:
                    
                    player_choice["X"] = currunt_player

                    player_choice["O"] = gamer2 if currunt_player == gamer1 else gamer1

                elif player_option == 2:

                    player_choice["O"] = currunt_player

                    player_choice["X"] = gamer2 if currunt_player == gamer1 else gamer1

                elif player_option == 3:
                    print("Final Scores")

                    print_scoreboard(score_board)

                    save_session(score_board)
                    break
                else:
                    print("Invalid choice. Try again.")
                    continue

                winner = single_game(options[player_option - 1], gamer1, gamer2, player_choice)
                if winner == 'D':
                    # Handle draw if needed

                    pass
                elif winner in score_board:
                    score_board[winner] += 1
                else:
                    print(f"Unexpected winner value: {winner}")

                print_scoreboard(score_board)
                currunt_player = gamer2 if currunt_player == gamer1 else gamer1

        elif choice == "2":
            
            history = load_session()
            if history:
                print("\n--- Past Game Play History ---")
                for key, value in history.items():
                    print(f"{key}: {value}")

        elif choice == "3":
            
            filename = input("Enter the filename of the session to view in browser (without extension): ")
            if os.path.exists(f"{filename}.html"):
                webbrowser.open(f"file://{os.path.abspath(f'{filename}.html')}")
            else:
                print("File not found.")

        elif choice == "4":
            
            for x in "Exiting the game. Goodbye!":
                print(x, end=" ")
                time.sleep(0.1)
            break

        else:
            print("Invalid choice. Try again.")
            print("hellow")

main()
