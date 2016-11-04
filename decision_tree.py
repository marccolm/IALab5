import numpy as np
from pprint import pprint
import sys

matrix = []
result = []
relation = {}

def get_instruction(input):
	if '%' in input:
		pass
	elif 'relation' in input:
		get_relation(input)
	elif 'attribute' in input:
		get_attribute(input[11:])
	elif 'data' in input:
		get_data(input)

def get_relation(input):
	pass

def get_data(input):
	for (i, line) in enumerate(sys.stdin):
		line = line.strip(" \n")
		if line is not "":
			matrix.append([])
			matrix[i] = line.split(",")

def get_attribute(input):
	attributes_enum = []
	attribute_dict = {}
	key = input.partition(" ")[0]
	attributes = input[len(key):]	
	attributes = attributes.strip("{ }\n")
	attributes = attributes.replace(" ", "")
	attributes = attributes.split(",")
	relation[key] = attributes
	for (i, attribute) in enumerate(attributes):
		relation[attribute] = i

def convert_matrix(matrix, relation):
	new_matrix = []
	for (i, row) in enumerate(matrix):
		new_matrix.append([])
		for (j, item) in enumerate(row):
			if j is len(row) - 1:
				print(matrix[i][j])
				#result.append(matrix[i][j])
				result.append(relation[item])
			else:
				new_matrix[i].append(relation[item])
	return new_matrix


if __name__ == "__main__":
	for line in sys.stdin:
		get_instruction(line)
	new_matrix = convert_matrix(matrix, relation)
	new_matrix = new_matrix[:len(new_matrix) - 1]
	print(new_matrix)
	print("Result")
	print(result)
	result = np.array(result)
	new_matrix = np.array(new_matrix)
	#print(recursive_split_function(new_matrix, result))
