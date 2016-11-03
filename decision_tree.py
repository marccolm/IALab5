import numpy as np
import sys

def get_instruction(input):
	if '%' in input:
		pass
	elif 'relation' in input:
		get_realation(input)
	elif 'attribute' in input:
		return get_attribute(input[11:])
	elif 'data' in input:
		return get_data(input)


def get_relation(input):
	pass

def get_data(input):
	pass

def get_attribute(input):
	relation = {}
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
	return relation


if __name__ == "__main__":
	for line in sys.stdin:
		relation = get_instruction(line)
		print(relation)