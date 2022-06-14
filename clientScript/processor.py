#from listening import listening
import json


def processor(inputchar):
	with open ("table.json") as json_data_file:
		table = json.load(json_data_file)

	inputchar = str(inputchar)
#	print(inputport)
	outputport = (table["client"][inputchar])
	return int((outputport))


if __name__ == "__main__":
		print(processor("b"))

