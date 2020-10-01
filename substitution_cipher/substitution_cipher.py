"""
Andrew Jiang
CyberSecurity


"""
import sys
import csv

filepath = ""
letters= "abcdefghijklmnopqrstuvwxyz"
reference = {}

def reference_setup():
# takes in a csv of the "baseline" frequencies and put it in a dictionary called reference
	with open ('reference.csv','r') as fp:
		for line in csv.reader(fp):
			reference[line[0].lower().strip()] = float(line[1])/100



def letter_freq(content):
# takes in a string and returns a dictionary of the frequency of each letter
	res = {}
	counter = 0

	for letter in letters:
		res[letter] = 0
		for char in content:
			if char in res:
				counter += 1
				res[char]+= 1
	for char in res:
		res[char] = res[char] / counter
	return res



def caesar_shift(content):
# takes a string of text and runs through all cases for a caesar shift
	possible_combo = {}
	for key in range(26):
		temp = ""
		for i in range(len(content)):
			if content[i] in letters:
				temp = temp + letters[(letters.index(content[i]) + key) % 26]
		possible_combo[temp] = freq_compare(letter_freq(temp))
	sort_dictionary = sorted(possible_combo.items(), key = lambda x: x[1], reverse = False)

	for i in sort_dictionary:
		print(i[0], i[1])
def freq_compare(cipher_dict):
# takes in a dictionary of letter frequencies, return a delta value compared with the baseline data
	lis = cipher_dict
	delta = 0.0
	for ele in lis:
		delta = delta + abs(lis[ele]- reference[ele])
	return delta


if __name__ == "__main__":
	filepath = str(sys.argv[1])
	reference_setup()
	with open(filepath, "r") as fp:
		cont = fp.read().lower()
	caesar_shift(cont)
