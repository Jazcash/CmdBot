import protocol

class CommandHandler():
	def __init__(self):
		self.socket = protocol.Protocol(address, port)
		self.cmd = {"hi":self.hi, "bye":self.bye}
	
	def addCmd(self, cmdFunction, cmdTrigger):
		if not (cmdTrigger): cmdTrigger = cmdFunction.__name__ # if no cmd trigger (e.g. !sayhi) is defined then use the function's name (!hi)
		self.cmd[cmdTrigger] = cmdFunction
		
	def executeCmd(self, trigger, channel, nick, user, cmd):
		return self.cmd[trigger](channel, nick, user, cmd[1:])
		
	## Jazbot Default Commands ##
	def authenticate(self, nick):
		self.ircConnection.send("USER "+nick+" "+nick+" "+nick+" "+" :I'm "+nick+"!\r\n")
		
	def register(self, nick):
		self.say("nickserv", nick)
		
	def say(self, where, msg):
		self.ircConnection.send("PRIVMSG "+where+" :"+msg+"\r\n")
		
	def setNick(self, nick):
		self.ircConnection.send("NICK "+nick+"\r\n")
		
	def joinChannels(self, channels):
		for channel in channels:
			self.ircConnection.send("JOIN :"+channel+"\r\n")
	
	def hi(self, channel, nick, user, cmdArgs):
		print "PRIVMSG "+channel+" :"+"boop"+"\r\n"
		
	def bye(self, channel, nick, user, cmdArgs):
		self.say("PRIVMSG "+channel+" :"+"boop"+"\r\n")