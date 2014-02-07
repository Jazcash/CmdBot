import string
import sys
import os
import threading
import inspect
import time
import commands
import ircFunctions
import defaultCommands

class CommandHandler:
	def __init__(self, ircFunctions):
		self.ircFunctions = ircFunctions
		
		self.cmds = {}
		self.funcs = {}
		self.setupCmds()
		
	def setupCmds(self):
		commands._say = self.ircFunctions.say
		commands._quit = self.ircFunctions.quit
		commands._join = self.ircFunctions.join
		commands._part = self.ircFunctions.part
		
		tmpCommands = inspect.getmembers(commands, inspect.isfunction) + inspect.getmembers(defaultCommands, inspect.isfunction)
		for cmd in tmpCommands:
			if (cmd[0][0] == "_"):
				self.cmds[cmd[0][1:]] = cmd[1]
			
		tmpCommands = inspect.getmembers(ircFunctions, inspect.isfunction)
		for cmd in tmpCommands:
			self.funcs[cmd[0]] = cmd[1]
		
	def execute(self, cmd, channel, userNick, userName):
		commands.user = userName
		commands.nick = userNick
		commands.channel = channel
		commands.args = cmd[1:]
		
		cmdName = cmd[0]
		
		print cmdName
		print self.cmds
		if (cmdName in self.cmds):
			self.cmds[cmdName]()