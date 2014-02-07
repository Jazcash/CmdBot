import string
import sys
import os
import threading
import inspect
import time
import commands.myCommands
import ircFunctions
import defaultCommands

class CommandHandler:
	def __init__(self, ircFunctions):
		self.ircFunctions = ircFunctions
		
		self.cmds = {}
		self.funcs = {}
		self.setupCmds()
		
	def setupCmds(self):
		commands.myCommands.ircSay = self.ircFunctions.say
		commands.myCommands.ircQuit = self.ircFunctions.quit
		commands.myCommands.ircJoin = self.ircFunctions.join
		commands.myCommands.ircPart = self.ircFunctions.part
		
		defaultCommands.ircQuit = self.ircFunctions.quit
		defaultCommands.ircJoin = self.ircFunctions.join
		defaultCommands.ircPart = self.ircFunctions.part
		
		tmpCommands = inspect.getmembers(commands.myCommands, inspect.isfunction) + inspect.getmembers(defaultCommands, inspect.isfunction)
		for cmd in tmpCommands:
			if (cmd[0][0] == "_"):
				self.cmds[cmd[0][1:]] = cmd[1]
			
		tmpCommands = inspect.getmembers(ircFunctions, inspect.isfunction)
		for cmd in tmpCommands:
			self.funcs[cmd[0]] = cmd[1]
		
	def execute(self, cmd, channel, userNick, userName):
		commands.myCommands.user = userName
		commands.myCommands.nick = userNick
		commands.myCommands.channel = channel
		commands.myCommands.args = cmd[1:]
		
		defaultCommands.user = userName
		defaultCommands.nick = userNick
		defaultCommands.channel = channel
		defaultCommands.args = cmd[1:]
		
		cmdName = cmd[0]
		
		if (cmdName in self.cmds):
			self.cmds[cmdName]()