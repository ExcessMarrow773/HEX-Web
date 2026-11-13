import string

def key_ring(key):
	abcs = [i for i in string.ascii_lowercase]
	
	for i in range(len(abcs)):
		if abcs[i] == key:
			key = i
			break
	abcs = abcs[i:]+abcs[:i]

	output = abcs
	return output

def main(text_input: str):
	input = text_input.lower().strip()

	print(key_ring("g"))

	output = input
	return output

if __name__ == "__main__":
	things = main("test")
	print(things)