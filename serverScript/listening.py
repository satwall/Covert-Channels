import scapy.all as scapy
from processor import processor

#netinterface = "enp0s3"
#portsrange = "tcp and portrange 50000-50200"

charline = ""

def returnportnum(pkt):
	if pkt['TCP'].flags == "F":
		dport = pkt.dport
#		return pkt['TCP'].dataofs
	try:
		char = (processor(dport))
		global charline
		
		if char != "\n":
			charline += char
		else:
			print charline
			f = open("output.txt","a")
			f.write(charline+"\n")
			f.close()
			charline = ""
	except:
		pass
		





def listening(netinterface,portsrange):
	print ("Start listening on" + portsrange)
	scapy.sniff(iface=netinterface,filter= portsrange,prn=returnportnum)



if __name__ == "__main__":
	listening()

