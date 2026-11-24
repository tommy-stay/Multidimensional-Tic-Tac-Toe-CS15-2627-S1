def display_grid(grid):
    print(grid[0][0], "|", grid[0][1], "|", grid[0][2])
    print("--+---+---")
    print(grid[1][0], "|", grid[1][1], "|", grid[1][2])
    print("--+---+---")
    print(grid[2][0], "|", grid[2][1], "|", grid[2][2])


def determine_winner(grid):
    if grid[0][0] == grid[0][1] == grid[0][2] and grid[0][0] != " ":
        return grid[0][0]

    if grid[1][0] == grid[1][1] == grid[1][2] and grid[1][0] != " ":
        return grid[1][0]

    if grid[2][0] == grid[2][1] == grid[2][2] and grid[2][0] != " ":
        return grid[2][0]

    if grid[0][0] == grid[1][0] == grid[2][0] and grid[0][0] != " ":
        return grid[0][0]

    if grid[0][1] == grid[1][1] == grid[2][1] and grid[0][1] != " ":
        return grid[0][1]

    if grid[0][2] == grid[1][2] == grid[2][2] and grid[0][2] != " ":
        return grid[0][2]

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != " ":
        return grid[0][0]

    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != " ":
        return grid[0][2]

    if grid[0][0] != " " and grid[0][1] != " " and grid[0][2] != " ":
        if grid[1][0] != " " and grid[1][1] != " " and grid[1][2] != " ":
            if grid[2][0] != " " and grid[2][1] != " " and grid[2][2] != " ":
                return "Tie"

    return "None"


grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

player = "X"

while determine_winner(grid) == "None":
    display_grid(grid)
    print()
    print("Player", player, "turn")
    print("Enter your move like this: 0,2")
    print()

    move = input("Enter row,column: ")

    if "," not in move:
        print("Please use a comma, like 0,2.")
        print()
        continue

    parts = move.split(",")

    if len(parts) != 2:
        print("Please enter only two numbers, like 0,2.")
        print()
        continue

    row = parts[0]
    column = parts[1]

    if row.isdigit() == False:
        print("The row must be a number.")
        print()
        continue

    if column.isdigit() == False:
        print("The column must be a number.")
        print()
        continue

    row = int(row)
    column = int(column)

    if row < 0 or row > 2:
        print("The row must be from 0 to 2.")
        print()
        continue

    if column < 0 or column > 2:
        print("The column must be from 0 to 2.")
        print()
        continue

    if grid[row][column] != " ":
        print("That space is already taken.")
        print()
        continue

    grid[row][column] = player

    if determine_winner(grid) == "None":
        if player == "X":
            player = "O"
        else:
            player = "X"

    print()

display_grid(grid)
print()

if determine_winner(grid) == "Tie":
    print("The game is a tie.")
else:
    print("Player", determine_winner(grid), "wins!")