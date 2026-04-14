def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
	mirror = []
	for l in matrix:
		new_l = []
		for i in range(len(l) - 1, -1, -1):
			new_l.append(l[i])
		mirror.append(new_l)
	return mirror

if __name__ == '__main__':
	print('================ Test Cases ================')
	print(f"mirror_matrix([[1, 2, 3], [4, 5, 6]]): {mirror_matrix([[1, 2, 3], [4, 5, 6]])}")
	print(f"mirror_matrix([[1, 2], [3, 4], [5, 6]]): {mirror_matrix([[1, 2], [3, 4], [5, 6]])}")
	print(f"mirror_matrix([[7]]): {mirror_matrix([[7]])}")
	print(f"mirror_matrix([[1, 2, 3, 4]]): {mirror_matrix([[1, 2, 3, 4]])}")
	print(f"mirror_matrix([[-1, -2], [-3, -4]]): {mirror_matrix([[-1, -2], [-3, -4]])}")