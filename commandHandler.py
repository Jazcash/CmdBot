import protocol
import string
import sys
import os
import threading
import commands
import inspect

class CommandHandler:
	def __init__(self, irc):
		self.irc = irc
		self.cmds = self.setupCmds()
		
	## SOCKET LOOP ##
	def socketLoop(self, func):
		#self.socketLoop = threading.Thread(target=self.irc.socketLoop, args=(func,))
		#self.socketLoop.daemon = False  # False = make socketLoop continue even after the userfile finishes
		#self.socketLoop.start()
		self.irc.socketLoop(func)
		
	def serverConnect(self, serverAddress, serverPort):
		self.irc.serverConnect(serverAddress, serverPort)
		
	def setupCmds(self):
		commands.say = self.say
		commands._quit = self._quit
		
		cmdDict = {}
		tmpCommands = inspect.getmembers(commands, inspect.isfunction)
		print tmpCommands
		for cmd in tmpCommands:
			cmdDict[cmd[0]] = cmd[1]
			print cmd[0]
		return cmdDict
		
	def execute(self, cmd, channel, userNick, userName):
		commands.user = userName
		commands.nick = userNick
		commands.channel = channel
		commands.args = cmd[1:]
		
		cmdName = cmd[0]
		
		if (cmdName in self.cmds):
			self.cmds[cmdName]()
		
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
			
	def _quit(self, userNick="Somebody"):
		print "Quitting"
		self.irc.send("QUIT :"+"%s called !quit" % (userNick)+" \r\n")
		sys.exit(1)