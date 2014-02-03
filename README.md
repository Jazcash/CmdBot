Jazbot
====

### About
Jazbot is an IRC bot API that allows users to easily add their own commands with straight-forward access to various metadata surrounding IRC like channels, users, nicknames, message etc.

### Dependancies
* Python 2.7

### Usage
```python
## myBot.py ##

import jazbot

mybot = jazbot.Jazbot("irc.w3.org", 6667, "Jazbot", ["#chan1"])

@mybot.addcmd("!hi")    # Trigger
def sayHi(nick):        # Your function
    print "Hello " + user + "!"
```
Then simply run your bot with: `$ python myBot.py`. That's all!

Now when a user (let's say bob) types __!hi__ in the same channel as your bot, your bot will respond with __hello bob!__ Easy!

### Documentation
#### Definitions
WIP

#### Code Definitions (Temporary - Will be moved later)
Sample IRC Message: `:JazcashRenamed!~Jazcash@public.cloak PRIVMSG #ectest :!hi Jim Fred`

Here are my code definitions (variable names) for the various parts of this message:

Socket Scope: `:<nick>!~<user>@<host> <signal> <signalArgs>`

The message is then parsed and because this is a PRIVMSG signal containing a command (`!hi`), the `Message Handler` sends these parts on to the `Command Handler` using the following names:

* nick = `"JazcashRenamed"`
* user = `"Jazcash"`
* channel = `"#ectest"`
* cmd = `["hi", "Jim", "Fred"]`

The first item in `cmd` is known as `cmdTrigger` and the collective name for the other items is `cmdArgs`.
