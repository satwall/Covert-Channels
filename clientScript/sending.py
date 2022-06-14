from scapy.all import *




def sendTCP(serverip,destport):
	packet = IP(dst=serverip)/TCP(dport=destport,flags="F")
	send(packet,verbose=False)





if __name__ == "__main__":
	while True:
		serverip = str(raw_input("Please Enter the Server's IP address \n"))
		destport = int(raw_input("Please Enter the destintion port \n"))
		sendTCP(serverip,destport)		