def string_permutation_checker(s1: str, s2: str) -> bool:
	if len(s1) != len(s2):
		return False
	for c in s1:
		if c in s2:
			s2 = s2[:s2.index(c)] + s2[s2.index(c) + 1:]
		else:
			return False
	return len(s2) == 0


if __name__ == '__main__':
	print('================ Test Cases ================')

	print(f'string_permutation_checker("abc", "bca"): {string_permutation_checker("abc", "bca")}')
	print(f'string_permutation_checker("abc", "def"): {string_permutation_checker("abc", "def")}')
	print(f'string_permutation_checker("listen", "silent"): {string_permutation_checker("listen", "silent")}')
	print(f'string_permutation_checker("hello", "bello"): {string_permutation_checker("hello", "bello")}')
	print(f'string_permutation_checker("", ""): {string_permutation_checker("", "")}')
	print(f'string_permutation_checker("a", ""): {string_permutation_checker("a", "")}')
	print(f'string_permutation_checker("Abc", "abc"): {string_permutation_checker("Abc", "abc")}')
	print(f'string_permutation_checker("a gentleman", "elegant man"): {string_permutation_checker("a gentleman", "elegant man")}')
