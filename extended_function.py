from S_DES import S_DES


def ASCII_S_DES(binary_array, key, inv=False):
	"""
	对待加密的二维int数组进行补零操作后加密
	:return: 加密后的二进制数组
	"""
	cipher_array = []
	for array in binary_array:
		while len(array) != 8:
			# 补0
			array = [0] + array
		cipher_array.append(S_DES(array, key, inv))
	return cipher_array


def extended_function(input_text, key, inv=False):
	"""
	:param input_text: 待加密的string
	:param key: 密钥
	:param inv: 是否为逆运算, 默认为False
	:return: 加密后的string
	"""
	# 将字符串转换为 ASCII 编码的数组
	ascii_array = [ord(char) for char in input_text]
	# 将每个ASCII码转换为二进制，然后拆分成单个二进制数字，并存储在数组中
	# 二维int数组,一维元素中有不满8位的
	binary_array = [[int(bit) for bit in bin(int(ascii_code))[2:]] for ascii_code in ascii_array]
	# 将二维int数组进行加密
	cipher_array = ASCII_S_DES(binary_array, key, inv)
	# 将每个二进制数组转换为整数，然后使用chr()函数转换为对应的ASCII字符
	ascii_characters = [chr(int(''.join(map(str, array)), 2)) for array in cipher_array]
	# 返回聚合在一起的字符串
	return ''.join(ascii_characters)


if __name__ == '__main__':
	# 第三关: 扩展功能
	input_text = "Hello, World!"
	key = [1, 0, 0, 0, 1, 0, 1, 1, 0, 1]
	ciphertext = extended_function(input_text, key)
	print(ciphertext)
	text = extended_function(ciphertext, key, True)
	print(text)
