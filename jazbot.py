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
		
		#self.cmdHandler.serverConnect(self.botAddress, botPort)
		self.setupAndStart()

	def setupAndStart(self):
		self.irc.serverConnect(self.botAddress, self.botPort)
		self.cmdHandler.authenticate(self.botNick) # authenticate session
		self.cmdHandler.setNick(self.botNick)  # set bot nick
		self.cmdHandler.say("nickserv", self.botNick) # register self with nickserv
		self.cmdHandler.joinChannels(self.botChannels) # join channels
		self.cmdHandler.socketLoop(self.msgHandler.parseMessages) # begin lisening to incoming messages