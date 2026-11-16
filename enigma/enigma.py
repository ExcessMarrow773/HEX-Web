import string

abcs = [i for i in string.ascii_lowercase]

def key_ring(key_index, letter):
	letter_index = abcs.index(letter)
	
	outer_abcs = abcs[key_index:]+abcs[:key_index]

	output = outer_abcs[letter_index]
	return output

def key_ring(key_index, letter):
	pass

def encode(text_input: str, keys: list):
	input = text_input.lower().strip()
	input = [i for i in input]
	outputv1 = []
	for i in range(len(input)):
		encrypted_stage = input[i]
		
		if input[i] in abcs:
			for key in keys:
				encrypted_stage = key_ring(abcs.index(key)+i, encrypted_stage)
		
		outputv1.append(encrypted_stage)


	print(input)
	
	output_string = ""
	
	for i in outputv1:
		output_string = output_string + i
	return output_string

def decode(encoded_input: str, keys: list):
	input = encoded_input.lower().strip()
	input = [i for i in input]
	outputv1 = []

	for i in range(len(input)):
		encrypted_stage = input[i]

		if input[i] in abcs:
			for key in keys:
				encrypted_stage = key_ring(abcs.index(key)+i, encrypted_stage)

		outputv1.append(encrypted_stage)


	print(input)

	output_string = ""

	for i in outputv1:
		output_string = output_string + i
	return output_string


if __name__ == "__main__":
	input = "zlac"
	things = decode(input, ["g"])	
	
	print(input)
	print(things)