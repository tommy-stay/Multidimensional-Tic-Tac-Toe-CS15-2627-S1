def display_grid(grid):
    print(grid[0][0], "|", grid[0][1], "|", grid[0][2])
    print("---+---+---")
    print(grid[1][0], "|", grid[1][1], "|", grid[1][2])
    print("---+---+---")
    print(grid[2][0], "|", grid[2][1], "|", grid[2][2])


def determine_winner(grid):
    if grid[0][0] == grid[0][1] == grid[0][2]:
        return grid[0][0]

    if grid[1][0] == grid[1][1] == grid[1][2]:
        return grid[1][0]

    if grid[2][0] == grid[2][1] == grid[2][2]:
        return grid[2][0]

    if grid[0][0] == grid[1][0] == grid[2][0]:
        return grid[0][0]

    if grid[0][1] == grid[1][1] == grid[2][1]:
        return grid[0][1]

    if grid[0][2] == grid[1][2] == grid[2][2]:
        return grid[0][2]

    if grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]

    if grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]

    return "Tie"

grid_1 = [
    ["X", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "O"]
]

grid_2 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "O", "X"]
]

grid_3 = [
    ["X", "O", "O"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]

grid_4 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"]
]

grids = [grid_1, grid_2, grid_3, grid_4]

for grid in grids:
    display_grid(grid)
    print()
    print("Winner:", determine_winner(grid))
    print()