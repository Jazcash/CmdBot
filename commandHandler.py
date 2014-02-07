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
		commands.ircSay = self.ircFunctions.say
		commands.ircQuit = self.ircFunctions.quit
		commands.ircJoin = self.ircFunctions.join
		commands.ircPart = self.ircFunctions.part
		
		defaultCommands.ircQuit = self.ircFunctions.quit
		defaultCommands.ircJoin = self.ircFunctions.join
		defaultCommands.ircPart = self.ircFunctions.part
		
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
		
		defaultCommands.user = userName
		defaultCommands.nick = userNick
		defaultCommands.channel = channel
		defaultCommands.args = cmd[1:]
		
		cmdName = cmd[0]
		
		if (cmdName in self.cmds):
			self.cmds[cmdName]()