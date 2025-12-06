import numpy as np
from abc import ABC

class Grid(ABC):
    def __init__(self, file_path) -> None:
        self.file_path = file_path

        self.grid = self.parse()

    @property
    def row_delimiter(self) -> str:
        return "\n"
    
    @property
    def col_delimiter(self) -> str:
        return ""

    def preprocess(self):
        return open(self.file_path, 'r').read()

    def parse(self) -> np.ndarray:
        file = self.preprocess()

        rows = file.split(self.row_delimiter)
        matrix = [t.split(self.col_delimiter) if self.col_delimiter != "" else list(t) for t in rows if t]
        return np.array(matrix)

        
    def __getitem__(self, position):
        i, j = position
        return self.grid[i, j]
    
    
    def display(self):
        for row in self.grid:
            print(' '.join(row))
    
    def get_neighbors(self, i, j):
        neighbors = []
        rows = len(self.grid)
        cols = len(self.grid[0]) if rows > 0 else 0
        
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    neighbors.append(self.grid[ni][nj])
        
        return neighbors
    

if __name__ == "__main__":
    test_path = "adventofcode2025/inputs/test_day6.txt"
    grid = Grid(test_path)

    grid.display()


    print(grid.get_neighbors(1, 1))  # Example usage