############# Available Variables #############		|		################ Available Functions #################
# user = username of person who typed command			|		# ircSay(channel, msg) = bot prints message in channel
# nick = nickname of person who typed command			|		# ircJoin(channels) = bot joins given channels
# channel = location that command was typed in		|		# ircQuit() = bot disconnects from IRC server
# args = arguments give to command								|		# ircPart(channels) = bot leaves given channels
# ==========================================================================================================
# If you function starts with an underscore, it will be interrpreted as a command with the function name
# as its trigger (minus the underscore). e.g. def _test(): ircSay(channel, "hello!") will print "hello" in
# the irc channel that any user calls the command '!test' in.

def _hi():
	ircSay(channel, "Hello %s!" % (nick))