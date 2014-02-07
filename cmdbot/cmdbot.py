import messageHandler
import socketHandler
import ircFunctions

class CmdBot:
	def __init__(self, botAddress="irc.w3.org", botPort=6667, botNick="Jazbot", botChannels=["#ectest"]):
		self.botAddress = botAddress
		self.botPort = botPort
		self.botNick = botNick
		self.botChannels = botChannels

		self.irc = socketHandler.SocketHandler(self.botAddress, self.botPort)
		self.ircFunctions = ircFunctions.IrcFunctions(self.irc)
		#self.cmdHandler = commandHandler.CommandHandler(self.ircFunctions)
		
		self.msgHandler = messageHandler.MessageHandler(self.ircFunctions)
		
		self.ircFunctions.authenticate(self.botNick) # authenticate session
		self.ircFunctions.setNick(self.botNick)  # set bot nick
		self.ircFunctions.say("nickserv", self.botNick) # register self with nickserv
		self.ircFunctions.join(self.botChannels) # join channels
		self.irc.listen(self.msgHandler.parseMessages) # begin lisening to incoming messages
		
if (__name__ == "__main__"):
	CmdBot()