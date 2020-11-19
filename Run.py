# Main Game Class

grind = [[None, None, None],
         [None, None, None],
         [None, None, None]]


def print_grid(grid):
    for i in grid:
        for j in i:
            if j is None:
                print(" ", end='')
            else:
                print(j, end='')
            print("|", end='')
        # New Line
        print("")


def quit_game():
    print("Thank you for playing Tic-Tac-Toe-Py")
    exit()


print("Welcome To Tic-Tac-Toe-Py")
if input("For rules press H, to start the game press any other key: ").lower() == "h":
    print("Rules are simple...")
    print("Get 3 of you symbol in a row vertically/horizontally or diagonally and you win")
    print("To select a box just enter the coordinates of the box starting from 1 1 at the top left corner")
    print("And ending on 3 3 at the bottom right corner")

    if input("Press any kay to continue or Q to quit: ").lower() == "q":
        quit_game()

# Max turns a game can have is 9
for i in range(1, 9):
    # Odd turn is X, even is O
    print("O turn") if i % 2 == 0 else print("X turn")
    print_grid(grind)
    validInput = False
    while not validInput:
        try:
            user_input = [int(x) for x in input("Enter the square you want to use: ").split()]
            if len(user_input) != 2:
                raise ValueError
            if not 0 < user_input[0] < 4 or not 0 < user_input[1] < 4:
                raise ValueError
        except ValueError as e:
            print("Bad Value please try again, you can only use values 1-3 inclusive")
            print("Used x y format for the coordinate separated by space")
            print("Example: 2 3")
            continue
        break

    print(user_input)
