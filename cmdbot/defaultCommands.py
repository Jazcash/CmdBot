############# Available Variables #############		|		################ Available Functions #################
# user = username of person who typed command			|		# ircSay(channel, msg) = bot prints message in channel
# nick = nickname of person who typed command			|		# ircJoin(channels) = bot joins given channels
# channel = location that command was typed in		|		# ircQuit(nick) = bot disconnects from IRC server
# args = arguments give to command								|		# ircPart(channel) = bot leaves given channel

def _join():
	ircJoin(args)
	
def _leave():
	ircPart(channel)
	
def _shutdown():
	ircQuit(nick)