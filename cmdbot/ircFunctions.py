import sys

class IrcFunctions:
	def __init__(self, irc):
		self.irc = irc

	def authenticate(self, nick):
		self.irc.send("USER "+nick+" "+nick+" "+nick+" "+" :I'm "+nick+"! \r\n")
		
	def register(self, nick):
		self.irc.send("nickserv", nick)
	
	def pong(self):
		self.irc.send("PONG")
		
	def say(self, where, msg):
		self.irc.send("PRIVMSG "+where+" :"+msg+" \r\n")
		
	def setNick(self, nick):
		self.irc.send("NICK "+nick+" \r\n")
		
	def join(self, channels):
		for channel in channels:
			self.irc.send("JOIN :"+channel+" \r\n")
			
	def part(self, channel):
		self.irc.send("PART :"+channel+" \r\n")
			
	def quit(self, nick):
		print("Quitting - %s called !quit" % (nick))
		self.irc.send("QUIT :"+"%s called !quit" % (nick)+" \r\n")
		sys.exit(1)