def twist_sequence(arr: list[int], k: int) -> list[int]:
	if len(arr) == 0:
		return []
	for i in range(k):
		temp = arr.pop()
		arr.insert(0, temp)
	return arr

if __name__ == '__main__':
	print('================ Test Cases ================')

	print(f'twist_sequence([1, 2, 3, 4, 5], 2): {twist_sequence([1, 2, 3, 4, 5], 2)}')
	print(f'twist_sequence([1, 2, 3], 1): {twist_sequence([1, 2, 3], 1)}')
	print(f'twist_sequence([1, 2, 3, 4], 0): {twist_sequence([1, 2, 3, 4], 0)}')
	print(f'twist_sequence([1, 2, 3], 5): {twist_sequence([1, 2, 3], 5)}')
	print(f'twist_sequence([], 3): {twist_sequence([], 3)}')