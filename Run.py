class ScoreTracker:
    # Scoring class
    # Positive score is X, negative score is 0
    # When a score of |3| a winner is announced

    grind = [[None, None, None],
             [None, None, None],
             [None, None, None]]

    def __init__(self):
        self.row = [0, 0, 0]
        self.col = [0, 0, 0]
        self.diag = [0, 0]

    def add_score(self, x, y, _player):
        player_value = 1 if _player == 'X' else -1
        self.row[x-1] += player_value
        self.col[y-1] += player_value
        if x in (1, 3):
            if y == x:
                self.diag[0] += player_value
            elif y in (1, 3):
                self.diag[1] += player_value

        if x == 2 and y == 2:
            self.diag[0] += player_value
            self.diag[1] += player_value

        for r in self.row:
            if abs(r) == 3:
                return "X" if r == 3 else "O"
        for c in self.col:
            if abs(c) == 3:
                return "X" if c == 3 else "O"
        for d in self.diag:
            if abs(d) == 3:
                return "X" if d == 3 else "O"
        return None


# Main Game Class
score_tracker = ScoreTracker()


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
    player = 'O' if i % 2 == 0 else 'X'
    print(player, " turn")
    print_grid(score_tracker.grind)
    validInput = False
    while not validInput:
        try:
            user_input = [int(x) for x in input("Enter the square you want to use: ").split()]
            if len(user_input) != 2:
                raise ValueError
            if not 0 < user_input[0] < 4 or not 0 < user_input[1] < 4:
                raise ValueError
            if score_tracker.grind[user_input[0] - 1][user_input[1] - 1] is not None:
                print("Grid space occupied, please try again")
                continue
        except ValueError as e:
            print("Bad Value please try again, you can only use values 1-3 inclusive")
            print("Used x y format for the coordinate separated by space")
            print("Example: 2 3")
            continue
        validInput = True
    score_tracker.grind[user_input[0] - 1][user_input[1] - 1] = player

    print(player, " has picked: ", user_input, "\n")

    winner = score_tracker.add_score(user_input[0], user_input[1], player)
    if winner is not None:
        print_grid(score_tracker.grind)
        print("The winner is player ", winner, "!!!!!")
        break
