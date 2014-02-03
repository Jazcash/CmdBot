import protocol
import string

class CommandHandler():
	def __init__(self, address, port, botNick, botChannels):
		self.socket = protocol.Protocol(address, port)
		self.cmd = {"hi":self.hi, "bye":self.bye, "quit":self.quit}
		
	## SOCKET LOOP ##
	def socketLoop(self, func):
		self.socket.socketLoop(func)

	def addCmd(self, cmdFunction, cmdTrigger):
		if not (cmdTrigger): cmdTrigger = cmdFunction.__name__ # if no cmd trigger (e.g. !sayhi) is defined then use the function's name (!hi)
		self.cmd[cmdTrigger] = cmdFunction
		
	def executeCmd(self, trigger, channel, nick, user, cmd):
		return self.cmd[trigger](channel, nick, user, cmd[1:])
		
	## Jazbot Default Commands ##
	def authenticate(self, nick):
		self.socket.send("USER "+nick+" "+nick+" "+nick+" "+" :I'm "+nick+"!\r\n")
		
	def register(self, nick):
		self.say("nickserv", nick)
		
	def say(self, where, msg):
		self.socket.send("PRIVMSG "+where+" :"+msg+"\r\n")
		
	def setNick(self, nick):
		self.socket.send("NICK "+nick+"\r\n")
		
	def joinChannels(self, channels):
		for channel in channels:
			self.socket.send("JOIN :"+channel+"\r\n")
	
	def hi(self, channel, nick, user, cmdArgs):
		self.say("Hello "+cmdArgs[1]+"!")
		
	def bye(self, channel, nick, user, cmdArgs):
		self.say("Goodbye "+nick+"!")

	def quit(self, channel, nick, user, cmdArgs):
		self.socket.send("QUIT :"+nick+" called !quit")
		print "%s (%s) called !quit. Shutting down..." % (nick, user)