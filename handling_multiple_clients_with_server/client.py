import socket
import threading
import sys

s = socket.socket()		  
port = int(input("Please enter the server's port number: "))
s.connect(('127.0.0.1', port))
print("Hi!\nPlease enter your name:")
while True:
	name = input()
	s.send(name.encode())
	massage = s.recv(1024).decode()
	if massage == "0":
		print("Sorry that name is used by another client!\nPlease enter your name again: ")
	else:
		break
print("1.List  2.Send  3.Receive  4.Exit")
def gettingCommand(s):
	while True:
		command = input()
		s.send(command.encode())
		if command == "4":
			return
def receive(s):
	while True:
		massage = s.recv(1024).decode()
		print(massage)
		if massage == "GoodBye!":
			return

while True:
	threadCommand = threading.Thread(target = gettingCommand, args = [s])
	threadReceive = threading.Thread(target = receive, args = [s])
	threadCommand.start()
	threadReceive.start()
	threadCommand.join()
	threadReceive.join()
	if not (threadCommand.isAlive() or threadReceive.isAlive()):
		sys.exit()