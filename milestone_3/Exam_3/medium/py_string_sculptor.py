
def string_sculptor(text: str) -> str:
	new_text = ""
	low = True
	for c in text:
		if c.isalpha():
			if low:
				new_text += c.lower()
				low = False
			else:
				new_text += c.upper()
				low = True
		else:
			new_text += c
	return new_text


if __name__ == '__main__':
	print('================ Test Cases ================')
	print(f'string_sculptor("hello"): {string_sculptor("hello")}')
	print(f'string_sculptor("Hello World"): {string_sculptor("Hello World")}')
	print(f'string_sculptor("aBc123def"): {string_sculptor("aBc123def")}')
	print(f'string_sculptor("Python3.9!"): {string_sculptor("Python3.9!")}')
	print(f'string_sculptor(""): {string_sculptor("")}')
