import socket
import threading


listOfClients = []
listOfCommands = []
s = socket.socket()	 
print ("Socket successfully created")
port = int(input("Enter the port number: "))
s.bind(('127.0.0.1', port))		 
print ("socket binded to %s" %(port))
s.listen(10)
print ("socket is listening")

def clientThread(conn, addr, listOfClients, listOfCommands):
	while True:
		name = conn.recv(1024).decode()
		try:
			listOfClients.index(name)
			conn.send("0".encode())
		except:
			listOfClients.append(conn)
			listOfClients.append(name)
			listOfCommands.append(conn)
			listOfCommands.append("nothing")
			conn.send("1".encode())
			break
	print("New connection:) : {}".format(name))
	while True:
		try:
			command = conn.recv(1024).decode()
			indx = listOfCommands.index(conn)
			listOfCommands[indx + 1] = command
			if command == "1":
				massage = ""
				count = 1
				for i in range(0, len(listOfClients), 2):
					if i != len(listOfClients) - 2:
						massage = massage + str(count) + ".Name: " + listOfClients[i + 1] + "\n"
					else:
						massage = massage + str(count) + ".Name: " + listOfClients[i + 1]
					count += 1
				conn.send(massage.encode())
			elif command == "2":
				conn.send("Please enter the name of the receiver and your massage:".encode())
				massage = conn.recv(1024).decode()
				indx = massage.index(" ")
				receiverName = massage[0:indx]
				massage = massage[indx + 1:]
				if receiverName != name:
					try:
						indx = listOfClients.index(receiverName)
						receiverConn = listOfClients[indx - 1]
						indx = listOfCommands.index(receiverConn)
						if listOfCommands[indx + 1] == "3":
							listOfCommands[indx + 1] = "0"
							indx = listOfClients.index(conn)
							massage = "You have new massage from " + listOfClients[indx + 1] + " : " + massage
						else:
							massage = "You have new massage: " + massage
						receiverConn.send(massage.encode())
						conn.send(("Your massage to {} is sent!".format(receiverName)).encode())
					except ValueError:
						conn.send("Sorry!That name is not in the list.".encode())
				else:
					conn.send("Invalid Receiver!You can't send massage to yourself!".encode())
			elif command == "3":
				pass
			elif command == "4":
				indx = listOfClients.index(conn)
				print("Connection {} left the chat! :(".format(listOfClients[indx + 1]))
				listOfClients.pop(indx)
				listOfClients.pop(indx)
				indx = listOfCommands.index(conn)
				listOfCommands.pop(indx)
				listOfCommands.pop(indx)
				conn.send("GoodBye!".encode())
				conn.close()
			else:
				conn.send("Wrong input!".encode())
		except:
			continue

while True:  
    conn, addr = s.accept()
    threadClient = threading.Thread(target = clientThread, args = [conn, addr, listOfClients, listOfCommands])
    threadClient.start()