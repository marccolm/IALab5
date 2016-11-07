import numpy as np
from pprint import pprint
import sys

matrix = []
result = []
relation = {}
keys = []
result_key = ""

def partition(a):
	return {c: (a==c).nonzero()[0] for c in np.unique(a)}

def entropy(s):
	res = 0
	val, counts = np.unique(s, return_counts=True)
	freqs = []
	for count in counts:
		freq = float(count) / len(s)
		freqs.append(freq)
	for p in freqs:
		if p != 0.0:
			res -= p * np.log2(p)
	return res



def get_instruction(input):
	if '%' in input:
		pass
	elif '@relation' in input:
		get_relation(input)
	elif '@attribute' in input:
		get_attribute(input[11:])
	elif '@data' in input:
		get_data(input)

def get_relation(input):
	pass

def get_data(input):
	for (i, line) in enumerate(sys.stdin):
		line = line.strip(" \n")
		if '%' in line:
			continue
		if line is not "":
			matrix.append(line.split(","))
			#matrix[i] = line.split(",")

def get_attribute(input):
	attributes_enum = []
	attribute_dict = {}
	key = input.partition("{")[0].strip(" \t\n")
	attributes = input[len(key):]   
	attributes = attributes.strip("{ }\n\t")
	attributes = attributes.replace(" ", "")
	attributes = attributes.split(",")
	relation[key] = attributes
	if not key in keys:
		keys.append(key)
		global result_key
		result_key = key

def convert_matrix(matrix, relation):
	new_matrix = []
	for (i, row) in enumerate(matrix):
		new_matrix.append([])
		for (j, item) in enumerate(row):
			if j is len(row) - 1:
				#print(matrix[i][j])
				#result.append(matrix[i][j])
				result.append(relation[keys[j]].index(item))
			else:
				new_matrix[i].append(relation[keys[j]].index(item))
	return new_matrix


if __name__ == "__main__":
	for line in sys.stdin:
		get_instruction(line)
	print(relation)
	new_matrix = convert_matrix(matrix, relation)
	new_matrix = new_matrix[:len(new_matrix) - 1]
	#print(relation)
	#print(new_matrix)
	#print("Result")
	#print(result)
	result = np.array(result)
	new_matrix = np.array(new_matrix)
	
	
