from typing import List

def read_puzzle_from_file(filename: str) -> List[List[int]]:
    """
    Read puzzle configuration from a file with consistent grid parsing
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        max_cols = max(len(line.strip().split()) for line in lines)
        
        puzzle = []
        for line in lines:
            row = []
            vals = line.strip().split()
            
            for val in vals:
                val = val.strip()
                if val == '':
                    row.append(' ')
                else:
                    try:
                        row.append(int(val))
                    except ValueError:
                        row.append(' ')
            
            while len(row) < max_cols:
                row.append(' ')
            
            if row:
                puzzle.append(row)
        
        return puzzle
