import socket
import sys
import string

class Protocol:
	def __init__(self, address, port):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serverConnect(address, port)
		
	def serverConnect(self, server, port):
		print "Connecting to: "+server+"...",
		try: 
			self.sock.connect((server, port))
			print "Connected!"
		except Exception, e:
			print "ERROR: "+e.args[1]
			sys.exit()
			
	def send(self, text):
		self.sock.send(text)
		
	def socketLoop(self, messageRetreived):
		print "Listening to incoming messages..."
		readbuffer = ""
		while 1:
			#readbuffer=readbuffer+self.sock.recv(510, socket.MSG_DONTWAIT & socket.MSG_PEEK) #Get non-blocking working
			readbuffer=readbuffer+self.sock.recv(510) # 510 bytes = max length of IRC message
			temp=string.split(readbuffer, "\r\n")
			readbuffer=temp.pop( )
			messageRetreived(temp)