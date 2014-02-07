# messageHandler.py
# Handles Messages - Parses then routes messages off to their correct destination
import commandHandler

class MessageHandler:
	def __init__(self, ircFunctions):
		self.ircFunctions = ircFunctions
		self.cmdHandler = commandHandler.CommandHandler(self.ircFunctions)
	
	def routeMessage(self, signal, userNick, userName):
		if ((len(signal) == 3) & (signal[0] == "PRIVMSG")): # if user types a command
			channel = signal[1]
			cmd = signal[2][1:].split(" ") # cmd[0] = cmdName, rest = cmdArgs
			if (signal[2][0] == "!"):
				self.cmdHandler.execute(cmd, channel, userNick, userName)
			else:
				self.ircFunctions.say(channel, signal[2])
		elif(signal[0] == "PING"):
			self.ircFunctions.pong() # when server pings, send back pong to stay alive (PONG <server>)
			
	def parseMessages(self, messages):
		for message in messages: # for every message in the received socket text, process its metadata
			print(message) # print all pre-parsed messages to console - debugging
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
					
			self.routeMessage(signalAndParams, user, nick) # send the message on to be processed