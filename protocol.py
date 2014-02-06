import socket
import string

class Protocol:
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	def serverConnect(self, serverAddress, serverPort):
		print "Connecting to: "+serverAddress+"...",
		self.sock.connect((serverAddress, serverPort))
		print "Connected!"
	
	def send(self, text):
		self.sock.send(text)
		
	def socketLoop(self, messageRetreived):
		print "Listening to incoming messages..."
		readbuffer = ""
		while 1:
			#readbuffer=readbuffer+self.sock.recv(510, socket.MSG_DONTWAIT & socket.MSG_PEEK) #Get non-blocking working
			readbuffer=readbuffer+self.sock.recv(510) # 510 bytes = max length of IRC message
			temp=string.split(readbuffer, "\r\n")
			readbuffer=temp.pop()
			messageRetreived(temp)