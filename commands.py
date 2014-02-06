############# Available variables #############
# user = username of person who typed command
# nick = nickname of person who typed command
# channel = location that command was typed in
# args = arguments give to command

def hi():
	_say(channel, "Hello %s!" % (nick))
	
def quit():
	_quit()