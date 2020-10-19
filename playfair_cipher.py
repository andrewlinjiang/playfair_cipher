import sys

key_dict = {}
key_grid = []
text_list = []

def key_parse(key): #takes in text and key, create 2d grid for key and list of twos for text
	for i in range (5):
		key_grid.append(key[i* 5:(i + 1)* 5])
	for j in range(len(key_grid)):
		key_grid[j] = list(key_grid[j])
	for x in range (5):
		for y in range (5):
			key_dict[key_grid[x][y]] = (x,y)


def text_parse(text):
	lis = []
	var = 1
	j = 0
	for i in text:
		if i =="J":
			lis.append("I")
		else:
			lis.append(i)
	while j < len(lis):
		if j % 2 == 0:
			if j + 1 < len(lis) and lis[j] == lis[j+1]:
				lis.insert(j+1, "X")
				j = 0
		j += 1
	if len(lis) % 2 != 0:
		lis.append("Z")
	for k in range(int(len(lis)/2)):
		text_list.append(lis[2*k]+ lis[2*k+1])


def playfair(text, key, process):
	res = ""
	key_parse(key)
	text_parse(text)
	print(key_dict)
	for duo in text_list:
		x0 = key_dict[duo[0]][0]
		y0 = key_dict[duo[0]][1]
		x1 = key_dict[duo[1]][0]
		y1 = key_dict[duo[1]][1]
		if x0 != x1 and y0 != y1:
			res += rect_swap(x0, y0, x1, y1)
		elif x0 == x1:
			res += row_swap(x0, y0, x1, y1, process)
		elif y0 == y1:
			res += column_swap(x0, y0, x1, y1, process)
	print(res)


def rect_swap(x0, y0, x1, y1):
	cip = key_grid[x0][y1] + key_grid[x1][y0]
	return cip


def row_swap(x0, y0, x1, y1, process):
	i = 0
	if process == "encode":
		i = 1
	if process == "decode":
		i = -1
	cip = key_grid[(x0 + i) % 5][y0] + key_grid[(x1 + i) % 5][y1]
	return cip


def column_swap(x0, y0, x1, y1, process):
	i = 0
	if process == "encode":
		i = 1
	if process == "decode":
		i = -1
	cip = key_grid[x0][(y0 + i) % 5] + key_grid[x1][(y1 + i )% 5]
	return cip
	
if __name__ == "__main__":
	process = str(sys.argv[1]).upper()
	text = str(sys.argv[2]).upper()
	key = str(sys.argv[3]).upper()
	playfair(text, key, process)
