import numpy as np
import sys

matrix = []
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
		print(line)
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
	for (i, row) in enumerate(matrix):
		for (j, item) in enumerate(row):
			#print(item)
			#print(relation[item])
			matrix[i][j] = relation[item]
	return matrix

if __name__ == "__main__":
	for line in sys.stdin:
		get_instruction(line)
	#print(matrix)
	#print(relation)
	new_matrix = convert_matrix(matrix, relation)
	print(new_matrix)