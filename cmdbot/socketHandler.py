import socket
import string
import signal
import sys

class SocketHandler:
	def __init__(self, serverAddress, serverPort):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serverConnect(serverAddress, serverPort)
	
	def serverConnect(self, serverAddress, serverPort):
		print "Connecting to: "+serverAddress+"...",
		self.sock.connect((serverAddress, serverPort))
		print "Connected!"
	
	def send(self, text):
		self.sock.send(text)
		
	def listen(self, messageRetreived):
		try:
			print "Listening to incoming messages..."
			readbuffer = ""
			while 1:
				#readbuffer=readbuffer+self.sock.recv(510, socket.MSG_DONTWAIT & socket.MSG_PEEK) # non-blocking test
				readbuffer=readbuffer+self.sock.recv(510) # 510 bytes = max length of IRC message
				temp=string.split(readbuffer, "\r\n")
				readbuffer=temp.pop()
				messageRetreived(temp)
		except KeyboardInterrupt:
			print " - Ctrl+C Pressed. Shutting down..."
			sys.exit(1)