# 简洁的代码无需注释
def P10(key):
	return [key[2], key[4], key[1], key[6], key[3], key[9], key[0], key[8], key[7], key[5]]


def P8(key):
	return [key[5], key[2], key[6], key[3], key[7], key[4], key[9], key[8]]


def Shift(key):
	return key[1:5] + key[:1] + key[6:] + key[5:6]


def IP(text):
	return [text[1], text[5], text[2], text[0], text[3], text[7], text[4], text[6]]


def IPinv(text):
	return [text[3], text[0], text[2], text[4], text[6], text[1], text[7], text[5]]


def EP(text):
	return [text[3], text[0], text[1], text[2], text[1], text[2], text[3], text[0]]


def XOR(text1, text2):
	return [t1 ^ t2 for t1, t2 in zip(text1, text2)]


S0 = [[[0, 1], [0, 0], [1, 1], [1, 0]],
      [[1, 1], [1, 0], [0, 1], [0, 0]],
      [[0, 0], [1, 0], [0, 1], [1, 1]],
      [[1, 1], [0, 1], [0, 0], [1, 0]]]

S1 = [[[0, 0], [0, 1], [1, 0], [1, 1]],
      [[1, 0], [1, 1], [0, 1], [0, 0]],
      [[1, 1], [0, 0], [0, 1], [1, 0]],
      [[1, 0], [0, 1], [0, 0], [1, 1]]]


def S(text):
	return S0[2 * text[0] + text[3]][2 * text[1] + text[2]] + S1[2 * text[4] + text[7]][2 * text[5] + text[6]]


def SP(text):
	return [text[1], text[3], text[2], text[0]]


def FK(R, key):
	return SP(S(XOR(EP(R), key)))


def SW(text):
	return text[4:] + text[:4]


def Round(text, key):
	return XOR(text[:4], FK(text[4:], key)) + text[4:]


def S_DES(text, key, inv=False):
	k1 = Shift(P10(key))
	if inv:
		return IPinv(Round(SW(Round(IP(text), P8(Shift(k1)))), P8(k1)))
	return IPinv(Round(SW(Round(IP(text), P8(k1))), P8(Shift(k1))))


if __name__ == '__main__':
	# 第一关: 基本测试
	text = [1, 1, 1, 1, 0, 0, 0, 0]
	print(text)
	key = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
	text_ = S_DES(text, key)
	print(text_)
	text__ = S_DES(text_, key, True)
	print(text__)
