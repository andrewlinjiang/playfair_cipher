run:
	@echo "make frequency : prints out the frequency of the letters given a file as an argument"
	@echo "make decode_caesar : decodes a monoalphabetic shift, takes in a txt file as ciphertext"
	@echo "make decode_substitution : suggests ciphertexts with greater "fitness" values, takes in a txt file as ciphertext"
analyze: frequency.py
	python3 frequency.py $(ARGS)

decode_caesar: caesar_cipher.py 
	python3 caesar_cipher.py $(ARGS)

decode_substitution: substitution_cipher.py
	python3 substitution_cipher.py $(ARGS)
