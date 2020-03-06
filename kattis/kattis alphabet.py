
def new_alphabet():
	inpt = input().lower()
	result = inpt
	alphabet = get_alphabet()
	for char in inpt:
		if find_letter(char, alphabet) == None:
			continue
		else:
			 result = result.replace(char, find_letter(char, alphabet))
			 #if len(find_letter(char, alphabet)) > 1:
			 	#inpt = result
	print(result)



def find_letter(letter, list):
	for i in range(len(list)):
		if letter == list[i][0]:
			return list[i][1]

 
def get_alphabet():
	list = [('a', '@'), ('b', '8'), ('c', '('), ('d', '|)'), ('e', '3'), ('f', '#'),
			('g', '6'), ('h', '[-]'), ('i', '|'), ('j', '_|'), ('k', '|<'), ('l', '1'),
			('m', '[]\/[]'), ('n', '[]\[]'),('o', '0'), ('p', '|D'), ('q', '(,)'), ('r', '|Z'),
			('s', '$'),('t', "']['"), ('u', '|_|'), ('v', '\/'), ('w', '\/\/'), ('x', '}{'), ('y', '`/'),
			('z', '2')]
	return list



new_alphabet()