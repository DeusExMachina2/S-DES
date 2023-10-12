from extended_function import extended_function
import threading
import time


def generate_all_possible_keys():
	"""
	生成所有可能的二进制密钥
	"""
	possible_keys = []
	for i in range(2 ** 10):
		binary_key = format(i, f'0{10}b')
		possible_keys.append([int(bit) for bit in binary_key])
	return possible_keys


def bruteforce_cracking_sub(keys, text, ciphertext, possible_keys_sub):
	"""
	暴力破解的并行子程序
	:param keys: 负责传回密钥
	:param text: 明文
	:param ciphertext: 密文
	:return: 与明密文对符合的密钥组
	:param possible_keys_sub: 可能的密钥组
	"""
	for k_guess in possible_keys_sub:
		if ciphertext == extended_function(text, k_guess):
			keys.append(k_guess)


def bruteforce_cracking(text, ciphertext):
	"""
	尝试暴力破解
	:param text: 明文
	:param ciphertext: 密文
	:return: 与明密文对符合的密钥组
	"""
	threads = []
	keys = []
	possible_keys = generate_all_possible_keys()
	idx = 0
	for i in range(4):
		sub_keys = threading.Thread(target=bruteforce_cracking_sub,
		                            args=(keys, text, ciphertext, possible_keys[idx:idx + 256]))
		threads.append(sub_keys)
		sub_keys.start()
		idx += 256
	for thread in threads:
		thread.join()
	# for k_guess in possible_keys():
	# 	if ciphertext == extended_function(text, k_guess):
	# 		keys.append(k_guess)
	return keys


if __name__ == '__main__':
	# 第四关: 暴力破解
	input_text = "H"
	key = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
	ciphertext = extended_function(input_text, key)
	# 尝试破解密钥, 开始计时
	start_time = time.perf_counter()
	cracked_key = bruteforce_cracking(input_text, ciphertext)
	elapsed_time = time.perf_counter() - start_time
	print(f"Cracked Key: \n{cracked_key}\nCost Time: {elapsed_time}")
	# 第五关: 封闭测试
	# 观察后易知,
	# P10操作将第1索引下的元素挪到第2索引下;
	# Shift操作会将第1、2索引下的元素挪到第0、1索引下;
	# P8操作不会使用第0、1索引下的元素.
	# 所以，在两次子密钥的生成时不会用到原密钥第1索引下的元素,
	# 对明文空间任意给定的明文分组，不论原密钥第1索引下的元素是多少都会生成相同密文.
	# 即对应明文空间任意给定的明文分组Pn，会出现选择不同的密钥Ki != Kj加密得到相同密文Cn的情况
