def display_board(board):
    print('\n'.join(['|'.join(board[i:i+3]) for i in range(0, 9, 3)]))

def player_input():
    while (marker := input("Player 1, choose X or O: ").upper()) not in 'XO':
        pass  # Wait until valid input
    return ('X', 'O') if marker == 'X' else ('O', 'X')

def place_marker(board, marker, position):
    board[position - 1] = marker

def win_check(board, mark):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(board[i] == mark for i in combo) for combo in wins)

import random

choose_first = lambda: 'Player 1' if random.random() < 0.5 else 'Player 2'
space_check = lambda board, position: board[position - 1] == ' '
replay = lambda: input("Play again? (y/n): ").lower().startswith('y')

def player_choice(board):
    while True:
        try:
            pos = int(input("Choose a position (1-9): "))
            if 1 <= pos <= 9 and space_check(board, pos):
                return pos
            print("Invalid or occupied position. Try again.")
        except ValueError:
            print("Invalid input.")

print('Welcome to Tic Tac Toe!')

while True:  # Outer game loop (for multiple games)
    board = [' '] * 9  # Create an empty board
    p1, p2 = player_input()  # Get player markers
    turn = choose_first()  # Determine who goes first
    print(f"{turn} goes first.")

    while True:  # Inner game loop (for a single game)
        marker = p1 if turn == 'Player 1' else p2  # Current player's marker
        display_board(board)  # Display the board
        pos = player_choice(board)  # Get player's move
        place_marker(board, marker, pos)  # Update the board

        if win_check(board, marker):  # Check for win
            display_board(board)
            print(f"Congratulations! {turn} wins!")
            break  # End the game
        elif ' ' not in board:  # Check for draw
            display_board(board)
            print("It's a draw!")
            break  # End the game

        turn = 'Player 2' if turn == 'Player 1' else 'Player 1'  # Switch turns

    if not replay():  # Ask to play again
        break  # Exit the outer loop if no replay