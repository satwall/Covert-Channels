import netifaces as nif


def get_iface():
	while True:
		ifaces =[]
		facenum = 0
		for iface in (nif.interfaces()):
	 		facenum += 1
	 		print (str(facenum) + " : " + str(iface))
	 		ifaces.append(iface)


		interface = str(raw_input("Which Interface do you want to use?\n"))
		if interface not in ifaces:
			print("Please choose the right interface. ")
			continue

		else:
			return (interface)
			break