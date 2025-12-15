import pytest
import numpy as np
import tempfile
import os
from commons.Grid import Grid


class TestGrid:
    """Test suite for the Grid class"""

    @pytest.fixture
    def simple_grid_file(self):
        """Create a temporary file with a simple grid"""
        content = "ABC\nDEF\nGHI"
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(content)
            temp_path = f.name
        yield temp_path
        os.unlink(temp_path)

    @pytest.fixture
    def numeric_grid_file(self):
        """Create a temporary file with a numeric grid"""
        content = "1 2 3\n4 5 6\n7 8 9"
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(content)
            temp_path = f.name
        yield temp_path
        os.unlink(temp_path)

    @pytest.fixture
    def single_row_file(self):
        """Create a temporary file with a single row"""
        content = "ABCDE"
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(content)
            temp_path = f.name
        yield temp_path
        os.unlink(temp_path)

    @pytest.fixture
    def empty_lines_file(self):
        """Create a temporary file with empty lines"""
        content = "ABC\n\nDEF\n\nGHI"
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(content)
            temp_path = f.name
        yield temp_path
        os.unlink(temp_path)

    def test_init_default_params(self, simple_grid_file):
        """Test Grid initialization with default parameters"""
        grid = Grid(simple_grid_file)
        assert grid.file_path == simple_grid_file
        assert grid.item_type == str
        assert grid.col_delimiter == ""
        assert grid.row_delimiter == "\n"
        assert grid.grid is not None

    def test_init_custom_params(self, numeric_grid_file):
        """Test Grid initialization with custom parameters"""
        grid = Grid(numeric_grid_file, col_delimiter=" ", item_type=int)
        assert grid.col_delimiter == " "
        assert grid.item_type == int
        assert isinstance(grid.grid, np.ndarray)

    def test_parse_simple_grid(self, simple_grid_file):
        """Test parsing a simple character grid"""
        grid = Grid(simple_grid_file)
        expected = np.array([['A', 'B', 'C'],
                            ['D', 'E', 'F'],
                            ['G', 'H', 'I']])
        np.testing.assert_array_equal(grid.grid, expected)

    def test_parse_numeric_grid(self, numeric_grid_file):
        """Test parsing a numeric grid with space delimiter"""
        grid = Grid(numeric_grid_file, col_delimiter=" ", item_type=int)
        expected = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])
        np.testing.assert_array_equal(grid.grid, expected)

    def test_parse_empty_lines_filtered(self, empty_lines_file):
        """Test that empty lines are filtered out during parsing"""
        grid = Grid(empty_lines_file)
        expected = np.array([['A', 'B', 'C'],
                            ['D', 'E', 'F'],
                            ['G', 'H', 'I']])
        np.testing.assert_array_equal(grid.grid, expected)

    def test_getitem(self, simple_grid_file):
        """Test __getitem__ method for accessing grid elements"""
        grid = Grid(simple_grid_file)
        assert grid[0, 0] == 'A'
        assert grid[0, 2] == 'C'
        assert grid[1, 1] == 'E'
        assert grid[2, 2] == 'I'

    def test_setitem(self, simple_grid_file):
        """Test __setitem__ method for modifying grid elements"""
        grid = Grid(simple_grid_file)
        grid[0, 0] = 'X'
        assert grid[0, 0] == 'X'
        grid[1, 1] = 'Y'
        assert grid[1, 1] == 'Y'

    def test_repr(self, simple_grid_file):
        """Test __repr__ method for string representation"""
        grid = Grid(simple_grid_file)
        repr_str = grid.__repr__()
        assert 'A B C' in repr_str
        assert 'D E F' in repr_str
        assert 'G H I' in repr_str

    def test_repr_numeric(self, numeric_grid_file):
        """Test __repr__ method with numeric grid"""
        grid = Grid(numeric_grid_file, col_delimiter=" ", item_type=int)
        repr_str = grid.__repr__()
        assert '1 2 3' in repr_str
        assert '4 5 6' in repr_str
        assert '7 8 9' in repr_str

    def test_repr_delimiter(self, simple_grid_file):
        """Test repr_delimiter property"""
        grid = Grid(simple_grid_file)
        assert grid.repr_delimiter == " "

    def test_get_neighbors_center(self, simple_grid_file):
        """Test get_neighbors for a center position"""
        grid = Grid(simple_grid_file)
        neighbors = grid.get_neighbors(1, 1)
        # Center position (1,1) = 'E' should have 8 neighbors
        assert len(neighbors) == 8
        expected_neighbors = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I']
        assert sorted(neighbors) == sorted(expected_neighbors)

    def test_get_neighbors_corner_top_left(self, simple_grid_file):
        """Test get_neighbors for top-left corner"""
        grid = Grid(simple_grid_file)
        neighbors = grid.get_neighbors(0, 0)
        # Top-left corner should have 3 neighbors
        assert len(neighbors) == 3
        expected_neighbors = ['B', 'D', 'E']
        assert sorted(neighbors) == sorted(expected_neighbors)

    def test_get_neighbors_corner_bottom_right(self, simple_grid_file):
        """Test get_neighbors for bottom-right corner"""
        grid = Grid(simple_grid_file)
        neighbors = grid.get_neighbors(2, 2)
        # Bottom-right corner should have 3 neighbors
        assert len(neighbors) == 3
        expected_neighbors = ['E', 'F', 'H']
        assert sorted(neighbors) == sorted(expected_neighbors)

    def test_get_neighbors_edge(self, simple_grid_file):
        """Test get_neighbors for an edge position"""
        grid = Grid(simple_grid_file)
        neighbors = grid.get_neighbors(1, 0)
        # Left edge (1,0) = 'D' should have 5 neighbors
        assert len(neighbors) == 5
        expected_neighbors = ['A', 'B', 'E', 'G', 'H']
        assert sorted(neighbors) == sorted(expected_neighbors)

    def test_get_neighbors_numeric_grid(self, numeric_grid_file):
        """Test get_neighbors with numeric grid"""
        grid = Grid(numeric_grid_file, col_delimiter=" ", item_type=int)
        neighbors = grid.get_neighbors(1, 1)
        # Center position should have 8 neighbors
        assert len(neighbors) == 8
        expected_neighbors = [1, 2, 3, 4, 6, 7, 8, 9]
        assert sorted(neighbors) == sorted(expected_neighbors)

    def test_copy(self, simple_grid_file):
        """Test copy method creates a new Grid instance"""
        grid = Grid(simple_grid_file)
        grid_copy = grid.copy()
        assert isinstance(grid_copy, Grid)
        assert grid_copy.file_path == grid.file_path
        # Note: The current copy implementation creates a new Grid,
        # so it will re-parse the file

    def test_preprocess(self, simple_grid_file):
        """Test preprocess method reads file content"""
        grid = Grid(simple_grid_file)
        content = grid.preprocess()
        assert content == "ABC\nDEF\nGHI"

    def test_single_row_grid(self, single_row_file):
        """Test grid with a single row"""
        grid = Grid(single_row_file)
        expected = np.array([['A', 'B', 'C', 'D', 'E']])
        np.testing.assert_array_equal(grid.grid, expected)

    def test_grid_shape(self, simple_grid_file):
        """Test that grid has correct shape"""
        grid = Grid(simple_grid_file)
        assert grid.grid.shape == (3, 3)

    def test_grid_shape_numeric(self, numeric_grid_file):
        """Test that numeric grid has correct shape"""
        grid = Grid(numeric_grid_file, col_delimiter=" ", item_type=int)
        assert grid.grid.shape == (3, 3)

    def test_display_no_error(self, simple_grid_file, capsys):
        """Test that display method runs without error"""
        grid = Grid(simple_grid_file)
        grid.display()
        captured = capsys.readouterr()
        assert 'A B C' in captured.out
        assert 'D E F' in captured.out
        assert 'G H I' in captured.out
