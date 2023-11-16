import random

# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

# Function to check if a number is safe to place in a given cell
def is_safe(grid, row, col, num):
    # Check row
    if num in grid[row]:
        return False

    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check 3x3 subgrid
    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[subgrid_row + i][subgrid_col + j] == num:
                return False

    return True

# Function to solve Sudoku using backtracking
def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Function to generate a Sudoku puzzle with a given difficulty level
def generate_sudoku(difficulty):
    # Create an empty 9x9 Sudoku grid
    grid = [[0 for _ in range(9)] for _ in range(9)]

    # Solve the Sudoku puzzle to get the solution
    solve_sudoku(grid)

    # Depending on the difficulty level, remove some numbers from the solved puzzle
    if difficulty == 'medium':
        for _ in range(35):
            row, col = random.randint(0, 8), random.randint(0, 8)
            while grid[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            grid[row][col] = 0
    elif difficulty == 'hard':
        for _ in range(50):
            row, col = random.randint(0, 8), random.randint(0, 8)
            while grid[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            grid[row][col] = 0

    return grid

# Main menu
while True:
    print("Sudoku Solver")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Quit")

    choice = input("Select a difficulty level or quit (1/2/3/4): ")
    
    if choice == '4':
        break

    if choice in ['1', '2', '3']:
        difficulty_levels = ['easy', 'medium', 'hard']
        difficulty = difficulty_levels[int(choice) - 1]

        puzzle = generate_sudoku(difficulty)

        print("Sudoku Puzzle:")
        print_grid(puzzle)

        if solve_sudoku(puzzle):
            print("\nSolved Sudoku:")
            print_grid(puzzle)
        else:
            print("No solution found.")
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")