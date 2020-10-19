import sys

def letter_shift(plaintext, key, dir):
	bleh = "abcdefghijklmnopqrstuvwxyz"
	return bleh[(bleh.index(plaintext) + (dir * bleh.index(key))) % 26]

def poly_cipher(type, text, key):
	res = ""
	if type == "decode":
		i = -1
	else:
		i = 1
	for j in range(len(text)):
		res += letter_shift(text[j], key[j % len(key)], i)
	print(res)




if __name__ == "__main__":
	type = str(sys.argv[1]).lower()
	text = str(sys.argv[2]).lower()
	key = str(sys.argv[3]).lower()
	poly_cipher(type, text, key)
	print(type)
