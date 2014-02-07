import protocol
import string
import sys
import os
import threading
import commands
import inspect
import time

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
		commands.IRCsay = self.IRCsay
		commands.IRCquit = self.IRCquit
		commands.IRCjoin = self.IRCjoin
		commands.IRCpart = self.IRCpart
		commands.IRCwait10 = self.IRCwait10
		
		cmdDict = {}
		tmpCommands = inspect.getmembers(commands, inspect.isfunction)
		for cmd in tmpCommands:
			cmdDict[cmd[0]] = cmd[1]
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
	def IRCauthenticate(self, nick):
		self.irc.send("USER "+nick+" "+nick+" "+nick+" "+" :I'm "+nick+"! \r\n")
		
	def IRCregister(self, nick):
		self.say("nickserv", nick)
	
	def IRCpong(self):
		self.irc.send("PONG")
		
	def IRCsay(self, where, msg):
		self.irc.send("PRIVMSG "+where+" :"+msg+" \r\n")
		
	def IRCsetNick(self, nick):
		self.irc.send("NICK "+nick+" \r\n")
		
	def IRCjoin(self, channels):
		for channel in channels:
			self.irc.send("JOIN :"+channel+" \r\n")
			
	def IRCpart(self):
		self.irc.send("PART :"+commands.channel+" \r\n")
			
	def IRCquit(self):
		print "Quitting - %s called !quit" % (commands.nick)
		self.irc.send("QUIT :"+"%s called !quit" % (commands.nick)+" \r\n")
		sys.exit(1)