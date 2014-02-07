import commandHandler
import messageHandler
import protocol

class Jazbot:
	def __init__(self, botAddress, botPort, botNick, botChannels):
		self.botAddress = botAddress
		self.botPort = botPort
		self.botNick = botNick
		self.botChannels = botChannels

		self.irc = protocol.Protocol()
		self.cmdHandler = commandHandler.CommandHandler(self.irc)
		self.msgHandler = messageHandler.MessageHandler(self.cmdHandler)
		
		self.setupAndStart()

	def setupAndStart(self):
		self.irc.serverConnect(self.botAddress, self.botPort)
		self.cmdHandler.IRCauthenticate(self.botNick) # authenticate session
		self.cmdHandler.IRCsetNick(self.botNick)  # set bot nick
		self.cmdHandler.IRCsay("nickserv", self.botNick) # register self with nickserv
		self.cmdHandler.IRCjoin(self.botChannels) # join channels
		self.cmdHandler.socketLoop(self.msgHandler.parseMessages) # begin lisening to incoming messages