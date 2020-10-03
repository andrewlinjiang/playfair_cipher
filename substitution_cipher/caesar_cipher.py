"""
Andrew Jiang
CyberSecurity


"""
from frequency import letter_freq
import sys
import csv

filepath = ""
letters= "abcdefghijklmnopqrstuvwxyz"
reference = {}

def reference_setup():
# takes in a csv of the "baseline" frequencies and put it in a dictionary called reference
	with open ('references/references.csv','r') as fp:
		for line in csv.reader(fp):
			reference[line[0].lower().strip()] = float(line[1])/100



def caesar_shift(content):
# takes a string of text and runs through all cases for a caesar shift
	possible_combo = {}
	for key in range(26):
		temp = ""
		for i in range(len(content)):
			if content[i] in letters:
				temp = temp + letters[(letters.index(content[i]) + key) % 26]
		possible_combo[temp] = freq_compare(letter_freq(temp), reference)

	sort_dictionary = sorted(possible_combo.items(), key = lambda x: x[1], reverse = False)

	for i in sort_dictionary:
		print(i[0], i[1])

def freq_compare(cipher_dict, reference):
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
