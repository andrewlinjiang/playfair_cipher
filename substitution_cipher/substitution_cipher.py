"""
Andrew Jiang
CyberSecurity
"""
from frequency import letter_freq
from caesar_cipher import freq_compare
import csv
import sys

filepath = ""
files = ["references", "bigram", "trigram", "words"]
data = {}

punct = ".,!"
def reference_setup():
	for name in files:
		temp = {}
		with open ('references/{}.csv'.format(name), 'r') as fp:
			for line in csv.reader(fp):
				temp[line[0].lower().strip()] = float(line[1])/100
		data["{}".format(name)] = temp

def substitution_cipher(cont):
	top_choice = ["e","t","a","i","o","n","s","r"]
	res = {} #returns potential plaintexts and their fitness level
	cipher_words = {} #holds a list of all the words in an array with number of occurance as value
	freq = letter_freq(cont) #frequency of all the letters
	fitness = freq_compare(freq, data["references"])

	temp = cont.lower().split(' ')
	for i in range(len(temp)):
		if temp[i][-1] in punct:
			tstring = temp[i][:-1]
		else:
			tstring = temp[i]
		if tstring not in cipher_words:
			cipher_words[tstring] = 1
		else:
			cipher_words[tstring] += 1

	#print(sorted(freq.values(), reverse = True)[0])
	for i in range(len(top_choice)):
		for ele in freq:
			if freq[ele] == sorted(freq.values(), reverse = True)[i]:
				lett = ele
		replaced = cont.replace(lett,top_choice[i])
		cipher_fitness = freq_compare(letter_freq(replaced), data["references"])
		if cipher_fitness < fitness:
			res[replaced] = cipher_fitness

	#finds and replaces one word elements with "a" or "i" then checks fitness
	arrg = {}
	for ele in cipher_words:
			for string in res:
				if len(ele) == 1:
					new1 = string.replace(ele, "a")
					arrg[new1] = freq_compare(letter_freq(new1), data["references"])
					new = string.replace(ele, "i")
					arrg[new] = freq_compare(letter_freq(new), data["references"])
			res.update(arrg)
	sort_dictionary = sorted(res.items(), key = lambda x: x[1], reverse = False)
	count = 0
	for i in sort_dictionary: 
		if(count <= 5):
			print(i[0], i[1])
			count = count + 1

if __name__ == "__main__":
	filepath = str(sys.argv[1])
	reference_setup()
	with open(filepath, "r") as fp:
		cont = fp.read().lower()
	substitution_cipher(cont)



