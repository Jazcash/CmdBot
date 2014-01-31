import protocol

class Jazbot:
	def __init__(self, address, port, nick="Jazbot", channels=["#ectest", "#ectest2"]):
		#Attributes
		self.nick = nick
		self.channels = channels
		
		#Setup bot
		self.setup(address, port)

	def setup(self, address, port):
		self.ircConnection = protocol.Protocol(address, port)
		self.authenticate(self.nick)
		self.setNick(self.nick)
		self.register(self.nick)
		self.joinChannels(self.channels)
		self.ircConnection.socketLoop(self.parseText)
		
	def say(self, msg, where):
		self.ircConnection.send("PRIVMSG "+where+" :"+msg)
		
	def authenticate(self, nick):
		self.ircConnection.send("USER "+nick+" "+nick+" "+nick+" "+" :I'm "+nick+"!\n")
		
	def register(self, nick):
		self.ircConnection.send("PRIVMSG nickserv :"+nick+"\r\n")    #auth
		
	def setNick(self, nick):
		self.ircConnection.send("NICK "+nick+"\n")
		
	def joinChannels(self, channels):
		for channel in channels:
			self.ircConnection.send("JOIN :"+channel+"\r\n")
			
	def parseText(self, text):
		textParts = text.split(" ")
		print "msg: "+text
		#status = textparts[1]
		#username = textparts[0].split("!")[0][1:]
		#location = textparts[
		#status = text.split(" ")[1]
		#if (status == "PRIVMSG"): # If received socket text is a user message
			#username = str(text.split(" ")[0].strip(":").split("!")[0])
			#location = username if (text.split(" ")[2] == self.nick) else text.split(" ")[2]
			#msg = text.split(":")[2].strip("\n").strip("\r")
			#print "status: "+status
			#print "username: "+username
			#print "who/location: "+location
			#print "msg: "+msg
			#print "==================="
			#print text
		#elif (status == "KICK"):
			#print text
		#else:
			#print text