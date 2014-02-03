import protocol
import time

class Jazbot:
	def __init__(self, address, port, nick, channels):
		#Attributes
		self.nick = nick
		self.channels = channels
		#Setup bot
		self.setupAndStart(address, port)

	def setupAndStart(self, address, port):
		self.ircConnection = protocol.Protocol(address, port) # connect to IRC server
		self.authenticate(self.nick) # authenticate session
		self.setNick(self.nick) # set bot nick
		self.register(self.nick) # register self with nickserv
		self.joinChannels(self.channels) # join channels
		self.ircConnection.socketLoop(self.parseMessages) # begin lisening to incoming messages
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
			
	def messageHandler(self, cmd, user=None, nick=None): # sends messages off to their appropriate handlers
		''' # unused for now
			Message Parts
					message["user"] # persistent for a session, is the user's nick at server join
					message["nick"] # can change during a session (i.e. /nick newname)
					message["cmd"] # first argument is the cmd name/code, others are parameters - msg text itself is /usually/ the last argument
		'''
		
		''' # example
		if (message["cmd"][0] == "PRIVMSG"):
			## MOVE BELOW PART TO PRIVMSG HANDLER ##
			if (message["cmd"][2].find("ACTION") > 0): # if message is an action (/me)
				print message["cmd"][2].replace("ACTION", message["nick"], 1)
			else: # if message isn't an action
				print message["nick"] + " said " + message["cmd"][len(message["cmd"])-1],
				if (message["cmd"][1] == self.nick): # if message was sent to me (Jazbot)
					print "to me"
				else: # if message was sent in a channel
					print "in "+message["cmd"][1]
					'''
		print message
	
	def parseMessages(self, messages):
		for message in messages: # for every message in the received socket text, process its metadata
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
			cmdAndParams = message[prefixEnd + 1:trailingStart].split(" ") # cmd and its paramaters are anything between prefix and trailing
			cmd = cmdAndParams[0] # cmd name/code itself is always the first item
			if (len(cmdAndParams) > 1):
					cmdparams = cmdAndParams[1:] # if cmd has paramaters, assign the parameters to their own variable
			if (trailing):
					cmdAndParams.append(trailing) # if there is a trailing, append it to the cmd paramaters
					
			''' Unused because it's easier/better to just pass the data as separate parameters instead
			## Create a handy message dictionary from the metadata ##
			message = {"cmd":cmdAndParams}
			if (prefix): message["prefix"] = prefix # not really used for anything as user and nick are passed on separately
			if (user): message["user"] = user
			if (nick): message["nick"] = nick
			'''
			
			self.messageHandler(cmd, user, nick) # send the message on to be processed
			
			if(cmdAndParams[0]=="PING"):
				self.ircConnection.send("PONG %s\r\n" % cmdAndParams[1]) # when server pings, send back pong to stay alive (PONG <server>)
				
			#time.sleep(1) # debugging