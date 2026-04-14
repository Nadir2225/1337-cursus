def number_base_converter(number: str, from_base: int, to_base: int) -> str:
	try:
		converted_num = ""
		max_base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		if to_base < 2 or from_base < 2 or to_base > 36 or from_base > 36 :
			return "ERROR"
		dec = int(number, from_base)
		while dec > 0:
			converted_num += max_base[dec % to_base]
			dec //= to_base
		return converted_num[::-1]
	except:
		return "ERROR"
	

if __name__ == '__main__':
	print('================ Test Cases ================')

	print(f'number_base_converter("1010", 2, 10): {number_base_converter("1010", 2, 10)}')
	print(f'number_base_converter("FF", 16, 10): {number_base_converter("FF", 16, 10)}')
	print(f'number_base_converter("255", 10, 16): {number_base_converter("255", 10, 16)}')
	print(f'number_base_converter("123", 10, 2): {number_base_converter("123", 10, 2)}')
	print(f'number_base_converter("Z", 36, 10): {number_base_converter("Z", 36, 10)}')
	print(f'number_base_converter("35", 10, 36): {number_base_converter("35", 10, 36)}')
	print(f'number_base_converter("123", 1, 10): {number_base_converter("123", 1, 10)}')
	print(f'number_base_converter("G", 16, 10): {number_base_converter("G", 16, 10)}')