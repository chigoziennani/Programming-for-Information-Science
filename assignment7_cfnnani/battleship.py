__author__ = 'Chigozie Nnani, cfnnani@unc.edu, Onyen = cfnnani'

import random

class BattleshipGame:
    # Initialize the game with one or two players and set opponents.
    def __init__(self, num_of_players):
        if num_of_players == 1:
            self.players = [HumanPlayer("Player 1"), ComputerPlayer("The Computer")]
        else:
            self.players = [HumanPlayer("Player 1"), HumanPlayer("Player 2")]

        self.players[0].set_opponent(self.players[1])
        self.players[1].set_opponent(self.players[0])

    # Main game loop to alternate turns between players until a winner is found.
    def play(self):
        self.players[0].position_fleet()
        self.players[1].position_fleet()

        input("The boats are ready... it's time to play.  Press enter to begin!")
        winner = False
        first_players_turn = True
        while not winner:
            if first_players_turn:
                winner = self.players[0].take_turn()
                if winner:
                    print("Game over!", self.players[0].player_name, "wins!")
            else:
                winner = self.players[1].take_turn()
                if winner:
                    print("Game over!", self.players[1].player_name, "wins!")
            first_players_turn = not first_players_turn

class Board:
    # Initialize a 10x10 grid for the game board and a hit counter.
    def __init__(self):
        self.grid = [[" _"] * 10 for _ in range(10)]
        self.hit_count = 0

    # Return a string representation of the board for display.
    def __str__(self):
        display = "  0 1 2 3 4 5 6 7 8 9\n"
        for i in range(10):
            display += str(i)
            for j in range(10):
                display += self.grid[i][j]
            if i != 9:
                display += "\n"
        return display

    # Return a public view of the board, hiding boat positions.
    def get_public_view(self):
        display = "  0 1 2 3 4 5 6 7 8 9\n"
        for i in range(10):
            display += str(i)
            for j in range(10):
                display += " _" if self.grid[i][j] == " B" else self.grid[i][j]
            if i != 9:
                display += "\n"
        return display

    # Attempt to add a boat to the board, checking for valid placement.
    def add_boat(self, boat):
        dx, dy = (boat.size, 1) if boat.orientation == "h" else (1, boat.size)
        if boat.x + dx > 10 or boat.y + dy > 10:
            return False
        for x in range(boat.size):
            xx = boat.x + (x if boat.orientation == "h" else 0)
            yy = boat.y + (x if boat.orientation == "v" else 0)
            if self.grid[yy][xx] != " _":
                return False
        for x in range(boat.size):
            xx = boat.x + (x if boat.orientation == "h" else 0)
            yy = boat.y + (x if boat.orientation == "v" else 0)
            self.grid[yy][xx] = " B"
        return True

    # Process an attack on the board at the given coordinates.
    def attack(self, x, y):
        if self.grid[y][x] == " B":
            self.grid[y][x] = " X"
            self.hit_count += 1
            return True
        elif self.grid[y][x] == " _":
            self.grid[y][x] = " O"
            return False
        return False
    # Check if all boats on the board have been hit.
    def is_defeated(self):
        return self.hit_count == 17

class Boat:
    # Initialize a boat with a label and size.
    def __init__(self, label, size):
        self.label = label
        self.size = size
        self.x = None
        self.y = None
        self.orientation = None
    # Set the position of the boat on the board.
    def set_position(self, x, y):
        self.x = x
        self.y = y

    # Set the orientation of the boat (vertical or horizontal).
    def set_orientation(self, orientation):
        self.orientation = orientation

class HumanPlayer:
    # Initialize a human player with a name, board, and fleet of boats.
    def __init__(self, player_name):
        self.player_name = player_name
        self.board = Board()
        self.fleet = [Boat("Aircraft Carrier", 5), Boat("Battleship", 4),
                      Boat("Submarine", 3), Boat("Destroyer", 3), Boat("Patrol Boat", 2)]
        self.opponent = None
        self.total_attacks = 0
        self.total_hits = 0
        self.total_misses = 0

    # Set the opponent for the player.
    def set_opponent(self, opponent):
        self.opponent = opponent

    # Allow the player to position their fleet on the board.
    def position_fleet(self):
        input(self.player_name + ": Are you ready to position your fleet?  Press enter to begin!")
        for boat in self.fleet:
            self.position_boat(boat)
        print("Your fleet is ready to play.  Your board is positioned as follows:")
        print(self.board)

    # Position a single boat on the board with user input.
    def position_boat(self, boat):
        print(self.board)
        print("You need to position a", boat.label, "of length", boat.size, "on the board above.")
        orientation = None
        while orientation not in ['v', 'h']:
            orientation = input("Would you like to use a vertical or horizontal orientation? (v/h) ")
        while True:
            try:
                pos = input("Please enter the position for the top-left location of the boat.  Use the form x,y (e.g., 1,3): ")
                x, y = map(int, pos.split(","))
                boat.set_orientation(orientation)
                boat.set_position(x, y)
                if self.board.add_boat(boat):
                    break
                else:
                    print("You must choose a position that is (a) on the board and (b) doesn't intersect with any other boats.")
            except:
                print("You must a valid position for the boat.  Please try again.")

    # Allow the player to take a turn by attacking the opponent's board.
    def take_turn(self):
        print(f"{self.player_name}'s board:")
        print(self.board)
        print()
        print(f"Your view of {self.opponent.player_name}'s board:")
        print(self.opponent.board.get_public_view())
        print(f"You have attacked {self.total_attacks} times, with {self.total_hits} hits and {self.total_misses} misses.")
        while True:
            try:
                pos = input("Please enter the position you would like to attack.  Use the form x,y (e.g., 1,3): ")
                x, y = map(int, pos.split(","))
                if not (0 <= x <= 9 and 0 <= y <= 9):
                    raise ValueError
                break
            except:
                print("You must a valid position in the form x,y where both x and y are integers in the range of 0-9. Please try again.")

        self.total_attacks += 1
        if self.opponent.board.attack(x, y):
            print("You hit a boat!")
            self.total_hits += 1
        else:
            print("You missed.")
            self.total_misses += 1
        return self.opponent.board.is_defeated()

class ComputerPlayer(HumanPlayer):
    # Initialize a computer player with a name and previous moves list.
    def __init__(self, player_name):
        super().__init__(player_name)
        self.previous_moves = []

    # Automatically position the computer's fleet on the board.
    def position_fleet(self):
        for boat in self.fleet:
            while True:
                orientation = random.choice(["v", "h"])
                x, y = random.randint(0, 9), random.randint(0, 9)
                boat.set_orientation(orientation)
                boat.set_position(x, y)
                if self.board.add_boat(boat):
                    break
        print("The Computer has positioned its fleet.")

    # Allow the computer to take a turn by randomly attacking the opponent's board.
    def take_turn(self):
        while True:
            x, y = random.randint(0, 9), random.randint(0, 9)
            if (x, y) not in self.previous_moves:
                self.previous_moves.append((x, y))
                break
        hit = self.opponent.board.attack(x, y)
        print(f"The computer attacked ({x},{y}) and", "hit a boat!" if hit else "missed.")
        return self.opponent.board.is_defeated()