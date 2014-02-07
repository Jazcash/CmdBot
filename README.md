Jazbot
====

### About
Jazbot is an IRC bot API that allows users to easily add their own commands with straight-forward access to various metadata surrounding IRC like channels, users, nicknames, message etc.

### Dependancies
* Python 2.7

### Usage
```python
## myBot.py ##
import cmdbot

mybot = cmdbot.CmdBot("irc.w3.org", 6667, "Jazbot", ["#chan1"])

## commands.py ##
def hi():
    _say(channel, "Hello %s!" % (nick))
```
Then simply run your bot with: `$ python myBot.py`. That's all!

Now when a user (let's say bob) types `!hi` in the same channel as your bot, your bot will respond with `Hello bob!` Easy!

### Documentation
#### Definitions
WIP

#### Code Definitions (Temporary - Will be moved later)
Sample IRC Message: `:JazcashRenamed!~Jazcash@public.cloak PRIVMSG #ectest :!hi Jim Fred`

Here are my code definitions (variable names) for the various parts of this message:

Level 1: 
`<prefix> <signal>`
```
prefix = :JazcashRenamed!~Jazcash@public.cloak` 
signal = PRIVMSG #ectest :!hi Jim Fred
```
	
Level 2: 
`:<nick>!~<user>@<host> <signalName> <signalArgs>`
```
nick = JazcashRenamed
user = Jazcash
host = public.cloak
signalName = PRIVMSG
signalArgs = ["#ectest", ":!hi Jim Fred"]
```
	
Levels below this are specific to the `PRIVMSG` signal

Level 3: 
`:<nick>!~<user>@<host> <signalName> <channel> :<text>`
```
text = !hi Jim fred
```
Levels below this are specific to chat commands

Level 4: 
`:<nick>!~<user>@<host> <signalName> <channel> :!<cmd>`
```
cmd = ["hi", "Jim", "Fred"]
```
Level 5: 
`:<nick>!~<user>@<host> <signalName> <channel> :!<cmdTrigger> <cmdArgs>`
```
cmdTrigger = hi
cmdArgs = ["Jim", "Fred"]
```
