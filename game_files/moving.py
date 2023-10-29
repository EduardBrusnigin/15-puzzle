from settings import MOUSE_STICKING


def find_zero(grid):
	for i in range(4):
		for j in range(4):
			if grid[i][j] == 0:
				return i, j


def is_possible(grid, cell_i, cell_j, mouse_ready):  # return True if move is possible else False
	zero_i, zero_j = find_zero(grid)

	if cell_i == zero_i and cell_j == zero_j:  # clicked cell is zero cell - return False
		return False

	if not MOUSE_STICKING:
		if not mouse_ready:
			return False

	return True  # return True if clicked cell is not zero


def move(grid, cell_i, cell_j):
	zero_i, zero_j = find_zero(grid)

	if cell_i == zero_i:  # clicked cell and zero cell in same row
		if cell_j < zero_j:  # clicked cell to the left of zero cell
			for k in range(zero_j-cell_j):  # sequential offset
				grid[cell_i][zero_j-k] = \
					grid[cell_i][zero_j-k-1]

		elif cell_j > zero_j:  # clicked cell to the right of zero cell
			for k in range(cell_j-zero_j):
				grid[cell_i][zero_j+k] = \
					grid[cell_i][zero_j+k+1]

		grid[cell_i][cell_j] = 0  # clicked cell becomes zero cell


	elif cell_j == zero_j:  # clicked cell and zero cell in same column
		if cell_i < zero_i:  # clicked cell is highter than zero cell
			for k in range(zero_i-cell_i):
				grid[zero_i-k][cell_j] = \
					grid[zero_i-k-1][cell_j]

		elif cell_i > zero_i:  # clicked cell is lower than zero cell
			for k in range(cell_i-zero_i):
				grid[zero_i+k][cell_j] = \
					grid[zero_i+k+1][cell_j]

		grid[cell_i][cell_j] = 0  # clicked cell becomes zero cell

	return grid
