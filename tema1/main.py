#Ciobanu Alin-Matei 335CB

import sys

def get_state(pattern, state, ch):
	if state < len(pattern) and ch == pattern[state]:
		return state + 1

	string = pattern[0:state] + ch # reprezinta sirul format pana in starea curenta + caracterul curent citit

	k = 1
	while (k < len(string)):
		# caut cel mai lung sufix care este prefix in pattern
		if pattern[0:(len(string) - k)] == string[k:len(string)]:
			return len(string) - k
		k += 1

	return 0

if __name__ == "__main__":
	f = open(sys.argv[1])
	g = open(sys.argv[2], "w")

	pattern = f.readline().rstrip("\n") #elimin "\n" din pattern
	text = f.readline().rstrip("\n")

	final_state = len(pattern)
	state = 0
	delta = {}

	for state in range(0, final_state + 1):
		for i in range(65, 91):
			ch = chr(i)
			delta[(state, ch)] = get_state(pattern, state, ch)

	state = 0
	for i in range(0, len(text)):
		state = delta[(state, text[i])]
		if state == final_state:
			g.write(str(i - final_state + 1))
			g.write(" ")

	g.write("\n")

	f.close()
	g.close()