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

def information_gain(y, x):
	#print("Y")
	#print(y)
	#print("X")
	#print(x)
	res = entropy(y)
	val, counts = np.unique(x, return_counts=True)
	freqs = []
	for count in counts:
		freq = float(count) / len(x)
		freqs.append(freq)

	for p, v in zip(freqs, val):
		res -= p * entropy(y[x == v])

	return res

def is_pure(s):
	return len(set(s)) == 1

def decision_tree(x, y, n):
	if is_pure(y) or len(y) == 0:
		for i in range(n): print(" "),
		print ("ANSWER: %s" % relation[result_key][y[0]])
		return

	gain = np.array([information_gain(y, x_attr) for x_attr in x.T])
	selected_attr = np.argmax(gain)

	if np.all(gain < 1e-6):
		for i in range(n): print(" "),
		print ("ANSWER: %s" % relation[result_key][y[0]])
		return

	sets = partition(x[:, selected_attr])

	for k, v in sets.items():
		y_subset = y.take(v, axis=0)
		x_subset = x.take(v, axis=0)

		for i in range(n): print(" "),
		print("%s: %s" % (keys[selected_attr], relation[keys[selected_attr]][k]))
		decision_tree(x_subset, y_subset, n+1)

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
	#print(relation)
	new_matrix = convert_matrix(matrix, relation)
	#print(relation)
	#print(new_matrix)
	#print("Result")
	#print(result)
	result = np.array(result)
	new_matrix = np.array(new_matrix)
	decision_tree(new_matrix, result, 0)
