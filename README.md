The goal of this assignment was to send a message from a client to a listening server through a covert channel. The application was written in Python 2.
To use the program, the following libraries are required:
Scapy
Netifaces
Json

To launch the application, use Python 2.7. 

The Server:
From the server directory, execute main.py by using the command "python main.py"
Choose the network interface you want to listen to. 
You can change the ports range to listen on in the main.py file, and to change the signal use modify the listening.py. 

The Client: 
From the client directory, execute main.py by using the command "python main.py"
Enter the IP Address of the server
Enter the message you want to send across the covert channel. 
You can use "-f" to specify a file which has the message you want to pass. 
