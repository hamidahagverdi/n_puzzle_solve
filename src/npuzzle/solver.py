import heapq
import copy
from typing import List, Tuple, Optional, Set

def find_blank(state: List[List[int]], n: int) -> Tuple[int, int]:
    """Find the position of the blank square"""
    for i in range(n):
        for j in range(n):
            if state[i][j] == ' ':
                return i, j
    raise ValueError(f"No blank square found in state: {state}")

def get_possible_moves(state: List[List[int]], n: int) -> List[List[List[int]]]:
    """Generate possible moves by moving the blank square"""
    blank_row, blank_col = find_blank(state, n)
    moves = []
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        new_row, new_col = blank_row + dr, blank_col + dc
        
        if 0 <= new_row < n and 0 <= new_col < n:
            new_state = copy.deepcopy(state)
            new_state[blank_row][blank_col] = new_state[new_row][new_col]
            new_state[new_row][new_col] = ' '
            moves.append(new_state)
    
    return moves

def manhattan_distance(state: List[List[int]], n: int) -> int:
    """Calculate Manhattan distance heuristic"""
    distance = 0
    for i in range(n):
        for j in range(n):
            if state[i][j] != ' ':
                target_num = state[i][j]
                target_row = (target_num - 1) // n
                target_col = (target_num - 1) % n
                distance += abs(i - target_row) + abs(j - target_col)
    return distance

def is_solvable(state: List[List[int]], n: int) -> bool:
    """Determine if the puzzle is solvable"""
    flat_state = [num for row in state for num in row if num != ' ']
    
    inversions = 0
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if flat_state[i] > flat_state[j]:
                inversions += 1
    
    if n % 2 == 1:
        return inversions % 2 == 0
    else:
        blank_row = n - find_blank(state, n)[0]
        return (inversions % 2 == 0) if blank_row % 2 == 1 else (inversions % 2 == 1)

class StateWrapper:
    """Wrapper class for state comparison in priority queue"""
    def __init__(self, f: int, g: int, state: List[List[int]], path: List[List[List[int]]]):
        self.f = f
        self.g = g
        self.state = state
        self.path = path
    
    def __lt__(self, other):
        return self.f < other.f

def solve_puzzle(initial_state: List[List[int]], goal_state: List[List[int]], n: int) -> Optional[List[List[List[int]]]]:
    """
    Solve the puzzle using A* search algorithm
    Returns the solution path if found, None otherwise
    """
    if not is_solvable(initial_state, n):
        return None
    
    start_node = StateWrapper(
        manhattan_distance(initial_state, n),
        0,
        initial_state,
        []
    )
    
    visited = set(tuple(map(tuple, initial_state)))
    frontier = [start_node]
    heapq.heapify(frontier)
    
    while frontier:
        current_node = heapq.heappop(frontier)
        current_state = current_node.state
        
        if current_state == goal_state:
            return current_node.path
        
        for move in get_possible_moves(current_state, n):
            move_tuple = tuple(map(tuple, move))
            
            if move_tuple in visited:
                continue
            
            visited.add(move_tuple)
            new_g = current_node.g + 1
            new_f = new_g + manhattan_distance(move, n)
            
            new_path = current_node.path + [move]
            new_node = StateWrapper(new_f, new_g, move, new_path)
            heapq.heappush(frontier, new_node)
    
    return None
