from listening import listening
from netiface import get_iface

###############################################################
#################### Configuration ############################
###############################################################
netinterface = get_iface()
portsrange = "tcp and portrange 50000-50200"




###############################################################


if __name__ == "__main__":
	listening(netinterface,portsrange) 