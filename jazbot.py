import time
import cmdHandler

class Jazbot:
	def __init__(self, address, port, botNick, botChannels):
		self.botNick = botNick
		self.botChannels = botChannels

		self.cmdHandler = cmdHandler.CommandHandler(address, port, botNick, botChannels)
		self.setupAndStart()

	def setupAndStart(self):
		self.cmdHandler.authenticate(self.botNick) # authenticate session
		self.cmdHandler.setNick(self.botNick)  # set bot nick
		self.cmdHandler.say("nickserv", self.botNick) # register self with nickserv
		self.cmdHandler.joinChannels(self.botChannels)
		self.cmdHandler.socketLoop(self.parseMessages) # begin lisening to incoming messages
			
	def messageHandler(self, cmd, userNick, userName): # sends messages off to their appropriate handlers based on conditions
		if ((cmd[0] == "PRIVMSG") & (cmd[len(cmd)-1][0] == "!")):
			channel = cmd[1]
			cmdArgs = cmd[2][1:].split(" ")
			self.cmdHandler.executeCmd(cmdArgs[0], channel, userNick, userName, cmd) # pass the cmd trigger (e.g. sayhi) to the cmd handler to be executed
			#trigger, channel, nick, user, cmd
			
	def parseMessages(self, messages):
		for message in messages: # for every message in the received socket text, process its metadata
			print message
			prefixEnd = -1	# prefix ends here
			trailingStart = len(message) # trailing starts here
			## Optional Variables - To make sure UnboundErrors don't occur ##
			prefix = None
			user = None
			nick = None
			trailing = None
			## Prefix ##
			if (message[0] == ":"): # if message starts with a prefix
				prefixEnd = message.find(" ")
				prefix = message[1:prefixEnd] # prefix ends at first occurce of a space
				## Username and Hostname ##
				prefixPartsNum = 0
				prefixParts = prefix.split("!")
				if (len(prefixParts) > 1 ):
					nick = prefixParts[0]
					prefixPartsNum = 1
					user = prefixParts[prefixPartsNum][1:].split("@")[0]
				hostname = prefixParts[prefixPartsNum]
			## Trailing ##
			trailingStart = message.find(" :") # trailing starts at first occurance of ' :'
			if (trailingStart >= 0): # if trailing was found
				trailing = message[trailingStart + 2:] # trailing is from where trailing begins+2 to the end of the message
			else:
				trailingStart = len(message) # otherwise there is no trailing, but keep track of where it would begin anyway for later use
			## Cmd + Cmd Params ##
			signalAndParams = message[prefixEnd + 1:trailingStart].split(" ") # cmd and its paramaters are anything between prefix and trailing
			signal = signalAndParams[0] # cmd name/code itself is always the first item
			if (len(signalAndParams) > 1):
					signalParams = signalAndParams[1:] # if cmd has paramaters, assign the parameters to their own variable
			if (trailing):
					signalAndParams.append(trailing) # if there is a trailing, append it to the cmd paramaters
					
			self.messageHandler(signalAndParams, user, nick) # send the message on to be processed
			
			if(signalAndParams[0]=="PING"):
				self.ircConnection.send("PONG %s\r\n" % signalAndParams[1]) # when server pings, send back pong to stay alive (PONG <server>)
				
			#time.sleep(1) # debugging