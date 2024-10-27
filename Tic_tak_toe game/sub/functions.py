#add module prt

import os
import webbrowser

# noughts and cross game interface

def game_interface(index):
    for x in range(0, 9, 3):
        print("\t\t     |     |     ")
        print(f"\t\t  {index[x]}  |  {index[x+1]}  |  {index[x+2]}  ")
        if x < 6:
            print("\t\t_____|_____|_____")
    print("\t\t     |     |     \n")

# make a function to win, draw

def inspect_win(index):
    winning_combination = [
        (0, 4, 8), (2, 4, 6), (0, 1, 2),
        (3, 4, 5), (6, 7, 8), (0, 3, 6),
        (1, 4, 7), (2, 5, 8)
    ]
    
    for (a, b, c) in winning_combination:
        if index[a] == index[b] == index[c] != " ":
            return True, index[a]
    
    if " " not in index:
        return True, " "
    
    return False, None

# Function to handle player moves

def make_move(index, player):
    while True:
        place = input(f"Player {player}, enter the position (0-8) or 'E' to exit: ").strip().upper()

        if place == "E":
            print("Exiting the game. Have a nice day!")
            exit()

        try:
            position = int(place)

            if index[position] == " ":
                index[position] = player
                break
            else:
                print("That cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

# save game session data in text file and HTML file

def save_session(session_stats):
    filename = input("Enter a filename to save the session (without extension): ")
    
    # text file part
    
    with open(f"{filename}.txt", "w") as file:
        for key, value in session_stats.items():
            file.write(f"{key}: {value}\n")
    
    # HTML file part
    
    with open(f"{filename}.html", "w") as file:
        file.write("<html><body>\n")
        file.write("<h1>Game Session Results</h1>\n")
        file.write("<table border='1'>\n<tr><th>Player</th><th>Score</th></tr>\n")
        for key, value in session_stats.items():
            file.write(f"<tr><td>{key}</td><td>{value}</td></tr>\n")
        file.write("</table>\n")
        file.write("</body></html>\n")

# load game session data from a text file

def load_session():
    filename = input("Enter the filename of the session to load (without extension): ")
    if os.path.exists(f"{filename}.txt"):
        with open(f"{filename}.txt", "r") as file:
            session_data = {}
            for line in file:
                key, value = line.split(": ")
                session_data[key] = int(value)
        return session_data
    else:
        print("File not found.")
        return None

# print the scoreboard

def print_scoreboard(score_board):
    for player, score in score_board.items():
        print(f"{player}: {score}")

# print the game main menu

def print_menu():
    print("\n\nMenu:")
    print("1. Play Game")
    print("2. View Past Game History")
    print("3. View Past Game History in Browser")
    print("4. Exit")

# Function to handle a game

def single_game(currunt_player, player1, player2, player_choice):
    index = [" " for _ in range(9)]

    while True:
        print("\n")

        game_interface(index)
        make_move(index, currunt_player)
        is_winner, winner = inspect_win(index)
        
        if is_winner:
            game_interface(index)
            
            if winner == ' ':
                print("It's a draw!")
                return 'D'  # Indicate a draw
            else:
                print(f"Player {player_choice[winner]} wins!")
                return player_choice[winner]
        currunt_player = 'O' if currunt_player == 'X' else 'X'
