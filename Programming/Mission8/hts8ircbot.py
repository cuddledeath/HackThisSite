# ASCII SHIFT HTS Mission 8
# https://www.hackthissite.org/missions/prog/8/
# You can link an irc nickname with a HTS account by typing: !link <hts account>
# in #perm8.
# Next your bot needs to connect to irc.hackthissite.org, and then it needs to
# notice moo with !perm8.
# Moo will notice you with !md5 <some random string> , your bot must reply with
# !perm8-result <hash>.
# If that is correct and done in time, moo will version the bot to check if you
# aren't using mIRC.
# Your bot MUST reply to the version. When that is correct, moo will notice you
# with !perm8-attack.
# When your bot receives that command it must join #takeoverz as fast as possible
# and attempt to kick moo (You will automatically be oped when you join
# the channel).
# Each month we will have a competition in #takeoverz to see who can control
# the channel the longest (See #takeoverz rules).
# The winner's source code will be on display on the site for people who have
# already completed the challenge.

# Import some necessary libraries.
import socket

# br.form['username'] = '********'
# br.form['password'] = '********'

# Some basic variables used to configure the bot
server = "irc.hackthissite.org"  # Server
channel = "#perm8"  # Channel
botnick = "********"  # Your bots nick
