from random import shuffle, choice

from settings import MIX_METHOD, NATURAL_MIX_ITERATIONS


def unnested_to_nested(unnested_grid):
	rows = [[], [], [], []]

	for i in range(4):
		for j in range(4):
			rows[i].append(unnested_grid[j+i*4])

	nested_grid = rows

	return nested_grid


def find_zero(grid):
	for i in range(4):
		for j in range(4):
			if grid[i][j] == 0:
				return i, j


def math_mix(grid):  # https://ru.wikipedia.org/wiki/Игра_в_15#Математическое_описание
	while True:
		shuffle(grid)

		N = 0

		for i in range(16):
			if grid[i] != 0:
				k = 0

				for j in range(15-i):
					if grid[i+j+1] != 0:
						if grid[i+j+1] < grid[i]:
							k += 1
				N += k

			elif grid[i] == 0:
				N += (i // 4) + 1  # N += number of zero row

		if N % 2 == 0:
			break

	return unnested_to_nested(grid)


def natural_mix(grid):
	# this method simulates real mixing. 
	# it is especially effective for large values of NATURAL_MIX_ITERATIONS in settings.py
	grid = unnested_to_nested(grid)

	zero_i, zero_j = find_zero(grid)


	for _ in range(NATURAL_MIX_ITERATIONS):
		possible_moves = []

		for i in range(4):  # search for all cells bordering a zero cell
			for j in range(4):
				if zero_i == i:
					if zero_j in (j+1, j-1):
						possible_moves.append([i, j])

				if zero_j == j:
					if zero_i in (i+1, i-1):
						possible_moves.append([i, j])

		random_cell = choice(possible_moves)

		i, j = random_cell[0], random_cell[1]

		grid[i][j], grid[zero_i][zero_j] = grid[zero_i][zero_j], grid[i][j]

		zero_i, zero_j = i, j

	return grid


def get_mixed():
	grid = [1, 2, 3, 4,
			5, 6, 7, 8,
			9, 10, 11, 12,
			13, 14, 15, 0]

	if MIX_METHOD == 1:
		return math_mix(grid)

	elif MIX_METHOD == 2:
		return natural_mix(grid)
