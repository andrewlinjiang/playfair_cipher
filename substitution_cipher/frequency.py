import sys

letters= "abcdefghijklmnopqrstuvwxyz"
freq = {}

def letter_freq(content):
# takes in a string and returns a dictionary of the frequency of each letter
    res = {}
    counter = 0

    for char in content:
        if char in letters and char not in res:
            res[char] = 0
        if char in res:
            counter += 1
            res[char]+= 1
    for char in res:
        res[char] = res[char] / counter
    return res

filepath = str(sys.argv[1])
with open(filepath, "r") as fp:
    cont = fp.read().lower()
freq = letter_freq(cont)

for ele in freq:
    print(ele, ":", freq[ele])
