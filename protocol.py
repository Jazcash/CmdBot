import socket
import sys

class Protocol:
	def __init__(self, address, port):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serverConnect(address, port)
		
	def serverConnect(self, server, port):
		print "Connecting to: "+server
		try: 
			self.sock.connect((server, port))
			print "Connected!"
		except Exception, e:
			print "ERROR: "+e.args[1]
			sys.exit()
			
	def send(self, text):
		self.sock.send(text)
		
	def socketLoop(self, textRetreived):
		while 1:
			text = self.sock.recv(2040)
			if (text.find("PING") != -1):
				self.send("PONG " + text.split() [1] + "\r\n")
				
			textRetreived(text)