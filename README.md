
---

# Building a Python Tic Tac Toe Game with Session Tracking and Scoreboard

Creating games in Python is a fun way to practice programming concepts while building something interactive. I recently developed a Tic Tac Toe game using Python that includes unique features like session tracking, scoreboards, and even the ability to save and view past game sessions in a web browser.

In this post, I'll share the process of creating this game, the features I added to make it more engaging, and a quick tutorial on how to play it yourself!

## Why Tic Tac Toe?

Tic Tac Toe is a classic game that’s easy to understand, but implementing it in code can be surprisingly challenging if you want to go beyond the basics. I wanted to create a game that allowed for a full gameplay experience with score tracking, saving and loading sessions, and an option to review past games in both text and HTML formats.

## Key Features of the Game

### 1. **Two-Player Support**

This game is designed for two players who take turns selecting a position on a 3x3 grid. Player 1 and Player 2 can choose to be "X" or "O" and switch symbols as they wish. The game interface displays the current state of the board after each turn.

### 2. **Real-Time Score Tracking**

The program updates the scores for both players at the end of each game. Wins draws, and losses are tracked throughout a game session so you can see how each player performs over multiple rounds.

### 3. **Session Saving and Loading**

One of the standout features is the ability to save and load game sessions. After each game session, scores are saved in both text and HTML formats. The HTML file can even be opened in a web browser for a nicely formatted view of past scores!

### 4. **View History in the Browser**

With the saved HTML session, you can look back at previous games directly from your browser. This is especially helpful if you want to track your progress over time or just review game history in an easy-to-read format.

## Under the Hood: How It Works

The game logic is organized into separate functions that handle core actions like checking for a win, making moves, and saving/loading data. Here’s a quick breakdown of the main parts of the game:

### Game Interface

The interface displays the Tic Tac Toe board and updates it in real time. After each move, the board updates to reflect the latest state, letting players see their positions.

```python
def game_interface(index):
    for x in range(0, 9, 3):
        print("\t\t     |     |     ")
        print(f"\t\t  {index[x]}  |  {index[x+1]}  |  {index[x+2]}  ")
        if x < 6:
            print("\t\t_____|_____|_____")
    print("\t\t     |     |     \n")
```



### Checking for Wins and Draws

![image](https://github.com/user-attachments/assets/6c9ce18f-2d7f-4b92-875d-10e398a5ed2b)


The game automatically checks for a win or draw after each move. If a player completes a row, column, or diagonal, the game ends and displays the winner’s name. Draws are also recognized if no more moves are possible.

### Saving and Loading Game Sessions

Each game session can be saved to a text or HTML file, allowing you to keep track of scores over time. Loading a session will pull up the saved data, so you can resume tracking scores or just look back at previous games.

```python
def save_session(session_stats):
    # Save session stats to .txt and .html files
```

## Playing the Game

To get started, run the main program in Python. You’ll be greeted with a menu that offers the following options:

1. **Play Game**: Start a new session and compete against another player.
2. **View Past Game History**: Load a previous session from a saved text file.
3. **View Past Game History in Browser**: Open a saved HTML file to view game results in your browser.
4. **Exit**: Quit the program.

Here's a preview of what the gameplay looks like:

```plaintext
Welcome to Tic Tac Toe!
Menu:
1. Play Game
2. View Past Game History
3. View Past Game History in Browser
4. Exit
```

## Final Thoughts

This project is a great starting point for anyone looking to learn about Python game development. It combines basic game logic with file handling and introduces features like real-time score tracking and session management. Tic Tac Toe is simple yet flexible enough to allow for these additions, making it an ideal project for beginner and intermediate Python developers alike.



---

