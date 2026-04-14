def compatibale(open: str, close: str) -> bool:
	if open == '[' and close == ']':
		return True
	if open == '(' and close == ')':
		return True
	if open == '{' and close == '}':
		return True
	return False

def bracket_validator(s: str) -> bool:
	closers = '])}'
	openers = '[({'
	open = []
	for c in s:
		if c not in closers and c not in openers:
			continue
		if len(open) == 0:
			if c in closers:
				return False
			if c in openers:
				open.append(c)
			continue
		if c in closers:
			if compatibale(open[-1], c):
				open.pop()
			else:
				return False
		if c in openers:
			open.append(c)
	if len(open) == 0:
		return True
	return False	


if __name__ == '__main__':
	print('================ Test Cases ================')
	
	print(f'bracket_validator("()"): {bracket_validator("()")}')
	s = "()[]{}"
	print(f'bracket_validator("{s}"): {bracket_validator("()[]{}")}')
	print(f'bracket_validator("(]"): {bracket_validator("(]")}')
	print(f'bracket_validator("([)]"): {bracket_validator("([)]")}')
	s = "{[]}"
	print(f'bracket_validator("{s}"): {bracket_validator("{[]}")}')
	s = "hello(world)[test]{code}"
	print(f'bracket_validator("{s}"): {bracket_validator("hello(world)[test]{code}")}')
	print(f'bracket_validator("((()))"): {bracket_validator("((()))")}')
	print(f'bracket_validator("((())"): {bracket_validator("((())")}')
	print(f'bracket_validator(""): {bracket_validator("")}')