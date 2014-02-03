import protocol

class CommandHandler():
	def __init__(self):
		self.cmd = {"hi":self.hi, "bye":self.bye}
	
	def addCmd(self, cmdFunction, cmdTrigger):
		if not (cmdTrigger): cmdTrigger = cmdFunction.__name__ # if no cmd trigger (e.g. !sayhi) is defined then use the function's name (!hi)
		self.cmd[cmdTrigger] = cmdFunction
		
	def executeCmd(self, trigger, channel, nick, user, cmd):
		self.cmd[trigger]()
		
	## Jazbot Default Commands ##
	def hi(self, channel, nick, user, args):
		("PRIVMSG "+channel+" :"+"boop"+"\r\n")
		
	def bye(self, channel, nick, user, args):
		("PRIVMSG "+channel+" :"+"boop"+"\r\n")