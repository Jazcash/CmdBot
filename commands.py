############# Available Variables #############		|		############### Available Functions ###############
# user = username of person who typed command			|		# say(channel, msg) = bot prints message in channel
# nick = nickname of person who typed command			|		# join(channels) = bot joins given channels
# channel = location that command was typed in		|		# quit() = bot disconnects from IRC server
# args = arguments give to command								|		# part(channels) = bot leaves given channels

def hi():
	say(channel, "Hello %s!" % (nick))
	
def shutdown():
	quit()
	
def join():
	join(args)
	
def part():
	part(args)