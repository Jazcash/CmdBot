############# Available Variables #############		|		################ Available Functions #################
# user = username of person who typed command			|		# IRCsay(channel, msg) = bot prints message in channel
# nick = nickname of person who typed command			|		# IRCjoin(channels) = bot joins given channels
# channel = location that command was typed in		|		# IRCquit() = bot disconnects from IRC server
# args = arguments give to command								|		# IRCpart(channels) = bot leaves given channels

def _say():
 	say()

def _join():
	join(args)
	
def _part():
	part()
	
def _quit():
	quit()