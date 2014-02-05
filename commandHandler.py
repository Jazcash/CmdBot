import protocol
import string

class CommandHandler:
	def __init__(self, irc):
		self.irc = irc
		self.cmds = {"hi":self.hi, "bye":self.bye, "quit":self.quit}
		
	## SOCKET LOOP ##
	def socketLoop(self, func):
		self.irc.socketLoop(func)

	def serverConnect(self, serverAddress, serverPort):
		self.irc.serverConnect(serverAddress, serverPort)
		
	def addCmd(self, cmdFunction, cmdTrigger):
		if not (cmdTrigger): cmdTrigger = cmdFunction.__name__ # if no cmd trigger (e.g. !sayhi) is defined then use the function's name (!hi)
		self.cmd[cmdTrigger] = cmdFunction
		
	def execute(self, cmd, channel, userNick, userName):
		cmdName = cmd[0]
		cmdArgs = cmd[1:]
		if cmdName in self.cmds:
			self.cmds[cmdName](cmdName, cmdArgs, channel, userNick, userName)
		
	## Jazbot Default Commands ##
	def authenticate(self, nick):
		self.irc.send("USER "+nick+" "+nick+" "+nick+" "+" :I'm "+nick+"! \r\n")
		
	def register(self, nick):
		self.say("nickserv", nick)
	
	def pong(self):
		self.irc.send("PONG")
		
	def say(self, where, msg):
		self.irc.send("PRIVMSG "+where+" :"+msg+" \r\n")
		
	def setNick(self, nick):
		self.irc.send("NICK "+nick+" \r\n")
		
	def joinChannels(self, channels):
		for channel in channels:
			self.irc.send("JOIN :"+channel+" \r\n")
	
	## User Chat Commands ##
	
	def hi(self, cmdName, cmdArgs, channel, userNick, userName):
		self.say(channel, "Hello "+userNick+"!")
		
	def bye(self, cmdName, cmdArgs, channel, userNick, userName):
		self.say(channel, "Goodbye "+userNick+"!")

	def quit(self, cmdName, cmdArgs, channel, userNick, userName):
		print "%s (%s) called !quit. Shutting down..." % (userNick, userName)
		self.irc.send("QUIT :"+"%s called !quit" % (userNick)+" \r\n")