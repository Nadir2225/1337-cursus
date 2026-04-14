def echo_validator(text: str) -> bool:
	if text == "":
		return False 
	reversed = [c for c in text.lower() if c.isalpha()]
	new_text = [c for c in text.lower() if c.isalpha()]
	reversed.reverse()
	return "".join(new_text) == "".join(reversed)


if __name__ == '__main__':
	print('================ Test Cases ================')
	print(f'echo_validator("racecar"): {echo_validator("racecar")}')
	print(f'echo_validator("A man a plan a canal Panama"): {echo_validator("A man a plan a canal Panama")}')
	print(f'echo_validator("race a car"): {echo_validator("race a car")}')
	print(f'echo_validator("Was it a car or a cat I saw"): {echo_validator("Was it a car or a cat I saw")}')
	print(f'echo_validator("hello"): {echo_validator("hello")}')
	print(f'echo_validator("Madam Im Adam"): {echo_validator("Madam Im Adam")}')
	print(f'echo_validator(""): {echo_validator("")}')