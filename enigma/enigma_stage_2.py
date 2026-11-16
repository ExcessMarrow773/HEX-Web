import string

abcs = [i for i in string.ascii_lowercase]

def key_ring(key_index, letter):
	letter_index = abcs.index(letter)
	
	outer_abcs = abcs[key_index:]+abcs[:key_index]

	output = outer_abcs[letter_index]
	return output

def main(text_input: str):
	input = text_input.lower().strip()
	input = [i for i in input]
	outputv1 = []
	keys = ["g", "d", "b"]

	for i in range(len(input)):
		outputv1.append(key_ring(abcs.index(keys[0])+i, input[i]))
		

	print(input)
	return outputv1

if __name__ == "__main__":
	things = main("test")
	print(things)