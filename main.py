from board_display import Board
from brain import Brain

board = Board()
brain = Brain()

print("\nWelcome to Tic-Tac-Toe!")
brain.ask_shape()
print(board.display)

end_game = False
while not end_game:
    brain.make_move()
    board.update_display(brain.matrix)
    print(board.display)
    if brain.is_win():
        print(f"\nCongratulations! Winner is Player {brain.whose_turn.shape}")
        replay = input("Do you want to play another round? (y/n): ").upper()
        while replay not in ['Y', 'N']:
            replay = input("Entry incorrect. Please try again.\nDo you want to play another round? (y/n): ").upper()
        if replay == 'Y':
            brain.reset()
            board.update_display(brain.matrix)
            brain.ask_shape()
            print(board.display)
        else:
            print("\nThanks for playing. See you next time!")
            end_game = True

# TODO: improvement would be to implement Single and Multi- player modes,
#       and create a computer "AI" that plays
#       Could be simple behaviour like play randomly, and play a counter whenever there is a two-alignment.

# TODO: ask name of the players at the beginning, or actually ask if they want to user names at all
