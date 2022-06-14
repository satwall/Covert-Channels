from sending import sendTCP
from processor import processor
from optparse import OptionParser





parser = OptionParser()

parser.add_option("-f","--file",dest="filename",help="file name")

(options,argrs) = parser.parse_args()

serverip = str(raw_input("Please Enter the Server's IP address \n"))


def sendmessage():
	message = str(raw_input("Message: ")+"\n")
	for char in message:
		destport = processor(char)
		sendTCP(serverip,destport)

	print("Message Sent")



if __name__ == "__main__":
	try:
		if len(options.filename) > 1:
		    filename = (options.filename)
		    print ("Using file name : "+str(filename) +"\n")
		    f = open ("message.txt","r")
		    message = (f.read())
		    for char in message:
			destport = processor(char)
			sendTCP(serverip,destport)
		    print ("Message Sent")		    
		else:
			while True:
				sendmessage()
	except:
		while True:
			sendmessage()


