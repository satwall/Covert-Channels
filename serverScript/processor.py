#from listening import listening
import json


def processor(inputport):
	with open ("table.json") as json_data_file:
		table = json.load(json_data_file)

	inputport = str(inputport)
#	print(inputport)
	outputchar = (table["server"][inputport])
	return (outputchar)


if __name__ == "__main__":
	while True:
		processor("50012")

