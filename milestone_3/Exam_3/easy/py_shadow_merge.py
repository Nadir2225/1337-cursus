def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
	list3 = list1 + list2
	list3.sort()
	return list3

if __name__ == '__main__':
	print('================ Test Cases ================')
	print(f'shadow_merge([1, 3, 5], [2, 4, 6]): {shadow_merge([1, 3, 5], [2, 4, 6])}')
	print(f'shadow_merge([1, 2, 3], [4, 5, 6]): {shadow_merge([1, 2, 3], [4, 5, 6])}')
	print(f'shadow_merge([1], [2, 3, 4]): {shadow_merge([1], [2, 3, 4])}')
	print(f'shadow_merge([], [1, 2, 3]): {shadow_merge([], [1, 2, 3])}')
	print(f'shadow_merge([1, 1, 2], [1, 3, 3]): {shadow_merge([1, 1, 2], [1, 3, 3])}')