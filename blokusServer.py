# server code courtesy of Kyle Chin and Rohan Varma
import socket
import threading
from queue import Queue
import random

HOST = "128.237.214.127" # put your IP address here if playing on multiple computers
PORT = 50110
BACKLOG = 4

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((HOST,PORT))
server.listen(BACKLOG)
print("looking for connection")

def handleClient(client, serverChannel, cID, clientele):
	client.setblocking(1)
	msg = ""
	while True:
		try:
			msg += client.recv(10).decode("UTF-8")
			command = msg.split("\n")
			while (len(command) > 1):
				readyMsg = command[0]
				msg = "\n".join(command[1:])
				serverChannel.put(str(cID) + " " + readyMsg)
				command = msg.split("\n")
		except:
			# we failed
			return

def serverThread(clientele, serverChannel):
	while True:
		msg = serverChannel.get(True, None)
		print("msg recv: ", msg)
		msgList = msg.split(" ")
		senderID = msgList[0]
		instruction = msgList[1]
		details = " ".join(msgList[2:])
		if (details != ""):
			for cID in clientele:
				if cID != senderID:
					sendMsg = instruction + " " + senderID + " " + details + "\n"
					clientele[cID].send(sendMsg.encode())
					print("> sent to %s:" % cID, sendMsg[:-1])
		print()
		serverChannel.task_done()


clientele = dict()
playerNum = 0

serverChannel = Queue(100)
threading.Thread(target = serverThread, args = (clientele, serverChannel)).start()

# shuffling courtesy of https://stackoverflow.com/questions/473973/shuffle-an-array-with-python-randomize-array-item-order-with-python
names = ["Reid", "Nico", "Seb", "Abhi"]
#names = random.shuffle(names)

while True:
	client, address = server.accept()
	# myID is the key to the client in the clientele dictionary
	myID = names[playerNum]
	print(myID, playerNum)
	for cID in clientele:
		print (repr(cID), repr(myID), repr(playerNum))

		clientele[cID].send(("newPlayer %d %s\n" % (names.index(myID), myID)).encode())
		client.send(("newPlayer %d %s\n" % (names.index(cID), cID)).encode())
	clientele[myID] = client
	client.send(("myIDis %d %s \n" % (names.index(myID), myID)).encode())
	print("connection recieved from %s" % myID)
	threading.Thread(target = handleClient, args = 
												(client ,serverChannel, myID, clientele)).start()
	playerNum += 1
