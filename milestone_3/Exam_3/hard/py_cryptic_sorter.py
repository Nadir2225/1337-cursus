def cryptic_sorter(strings: list[str]) -> list[str]:
	vowels = "aeiouAEIOU"

	def vowls_count(word: str) -> int:
		count = 0
		for c in word:
			if c in vowels:
				count += 1
		return count
	return sorted(
		strings,
		key=lambda s: (
			len(s),
			s.lower(),
			s.islower(),
			vowls_count(s)
		)
	)

if __name__ == '__main__':
	print('================ Test Cases ================')

	print(f'cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]): {cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"])}')
	print(f'cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]): {cryptic_sorter(["aaa", "bbb", "AAA", "BBB"])}')
	print(f'cryptic_sorter(["hello", "world", "hi", "test"]): {cryptic_sorter(["hello", "world", "hi", "test"])}')
	print(f'cryptic_sorter([]): {cryptic_sorter([])}')
	print(f'cryptic_sorter([""]): {cryptic_sorter([""])}')
