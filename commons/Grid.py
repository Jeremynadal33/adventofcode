import numpy as np
from abc import ABC

class Grid(ABC):
    def __init__(self, file_path, col_delimiter = "", row_delimiter = "\n", item_type = str) -> None:
        self.file_path = file_path
        self.item_type = item_type

        self.col_delimiter = col_delimiter
        self.row_delimiter = row_delimiter

        self.grid = self.parse()

    @property
    def repr_delimiter(self) -> str:
        return " "
    
    def copy(self):
        new_grid = Grid(self.file_path)
        return new_grid
    
    def preprocess(self):
        return open(self.file_path, 'r').read()

    def parse(self) -> np.ndarray:
        file = self.preprocess()

        rows = file.split(self.row_delimiter)
        matrix = [[self.item_type(item) for item in t.split(self.col_delimiter)] if self.col_delimiter != "" else list(self.item_type(t)) for t in rows if t]
        return np.array(matrix)

        
    def __getitem__(self, position):
        i, j = position
        return self.grid[i, j]
    
    def __setitem__(self, position, value):
        i, j = position
        self.grid[i, j] = value
    
    def __repr__(self) -> str:
        repr_str = ""
        for row in self.grid:
            if self.item_type != str:
                row = map(str, row)
            repr_str += self.repr_delimiter.join(row) + "\n"
        return repr_str
    
    def display(self):
        print(self.__repr__())
    
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