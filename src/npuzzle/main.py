import sys
from .puzzle import NPuzzle
from .utils import read_puzzle_from_file

def main():
    # Check if filename is provided as command-line argument
    if len(sys.argv) < 2:
        print("Usage: python -m npuzzle.main <input_file>")
        sys.exit(1)
    
    # Read puzzle from file
    puzzle_file = sys.argv[1]
    try:
        initial_state = read_puzzle_from_file(puzzle_file)
    except FileNotFoundError:
        print(f"Error: File '{puzzle_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading puzzle file: {e}")
        sys.exit(1)
    
    # Create puzzle solver
    puzzle = NPuzzle(initial_state)
    
    # Solve the puzzle
    print("Solving puzzle...")
    solution = puzzle.solve()
    
    # Output results
    if solution is None:
        print("No solution exists for this puzzle.")
    else:
        print(f"\nPuzzle solved in {len(solution)} moves!")
        print("\nSolution Path:")
        for i, state in enumerate(solution, 1):
            print(f"\nMove {i}:")
            for row in state:
                print(' '.join(str(val) for val in row))

if __name__ == "__main__":
    main()
