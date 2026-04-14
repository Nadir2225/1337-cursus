def pattern_tracker(text: str) -> int:
	consecutive = 0
	for i in range(len(text) - 1):
		c = text[i]
		c2 = text[i + 1]
		if c.isnumeric() and c2.isnumeric():
			if int(c2) - int(c) == 1:
				consecutive += 1
	return consecutive


if __name__ == '__main__':
	print('================ Test Cases ================')

	print(f'pattern_tracker("123"): {pattern_tracker("123")}')
	print(f'pattern_tracker("12a34"): {pattern_tracker("12a34")}')
	print(f'pattern_tracker("987654321"): {pattern_tracker("987654321")}')
	print(f'pattern_tracker("01234567"): {pattern_tracker("01234567")}')
	print(f'pattern_tracker("abc"): {pattern_tracker("abc")}')
	print(f'pattern_tracker("1a2b3c4"): {pattern_tracker("1a2b3c4")}')
	print(f'pattern_tracker("112233"): {pattern_tracker("112233")}')
