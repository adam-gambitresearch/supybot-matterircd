###
# Copyright (c) 2016, Gambit Research
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.ircmsgs as ircmsgs
import supybot.callbacks as callbacks

import time 

USERNAME = ''
PASSWORD = ''

class MatterIrcd(callbacks.Plugin):
    """This plugin allows supybot to authenticate with mattermost. It (probably
    doesn't expose any commands."""
    def __init__(self, irc):
        self.__parent = super(MatterIrcd, self)
        self.__parent.__init__(irc)
        self.log.info("MatterIrcd loaded")

    def reset(self, *args, **kwargs):
        pass

    #  We choose this as a clue that we've connected to the server to trigger
    #  authentication.
    #  376 RPL_ENDOFMOTD
    #    ":End of /MOTD command"
    def do376(self, irc, msg):
        self.log.info("Matterircd: Authenticating in response to: %r", msg)
        time.sleep(0.1)
        irc.sendMsg(ircmsgs.privmsg('mattermost', 'login %s %s' % (USERNAME, PASSWORD)))

Class = MatterIrcd

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
