def whisper_cipher(text: str, shift: int) -> str:
	if text == "":
		return "" 
	cipher = ""
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	for c in text:
		if c.isalpha():
			index = alpha.index(c.lower()) + shift
			while (index > 25):
				index -= 26
			if c.isupper():
				cipher += alpha[index].upper()
			else:
				cipher += alpha[index]

		else:
			cipher += c
	return cipher

if __name__ == '__main__':
	print('================ Test Cases ================')
	print(f'whisper_cipher("hello", 3): {whisper_cipher("hello", 3)}')
	print(f'whisper_cipher("Hello World!", 1): {whisper_cipher("Hello World!", 1)}')
	print(f'whisper_cipher("xyz", 3): {whisper_cipher("xyz", 3)}')
	print(f'whisper_cipher("ABC123def", 5): {whisper_cipher("ABC123def", 5)}')
	print(f'whisper_cipher("", 10): {whisper_cipher("", 10)}')