# -*- coding: utf-8 -*-
import praw
import OAuth2Util
import time

UA = "Shrug fixer by /u/AtomicEleven"
r = praw.Reddit(UA)
o = OAuth2Util.OAuth2Util(r)
reply = """**TL;DR:**  Type in ¯\\\\\\\\\\\\\\_(ツ)\\_/¯ for proper formatting

Actual reply:

For the 

    ¯\_(ツ)_/¯ 

like you were trying for you need three backslashes, so it should look like this when you type it out

    ¯\\\\\_(ツ)_/¯ 

which will turn out like this

¯\\\\\_(ツ)\_/¯ 

The reason for this is that the underscore character (this one \\_ ) is used to italicize words just like an asterisk does (this guy \\* ).  Since the "face" of the emoticon has an underscore on each side it naturally wants to italicize the "face" (this guy (ツ) ).  The backslash is reddit's escape character (basically a character used to say that you don't want to use a special character in order to format, but rather you just want it to display).  So your first "\\\\_" is just saying "hey, I don't want to italicize (ツ)" so it keeps the underscore but gets rid of the backslash since it's just an escape character.  After this you still want the arm, so you have to add two more backslashes (two, not one, since backslash is an escape character, so you need an escape character for your escape character to display--confusing, I know).  Anyways, I guess that's my lesson for the day on reddit formatting lol

***CAUTION: Probably very boring edit as to why you don't need to escape the second underscore, read only if you're super bored or need to fall asleep.***

Edit: The reason you only need an escape character for the first underscore and not the second is because the second underscore (which doesn't have an escape character) doesn't have another underscore with which to italicize.  Reddit's formatting works in that you need a special character to indicate how you want to format text, then you put the text you want to format, then you put the character again.  For example, you would type \_italicize\_ or \*italicize\* in order to get _italicize_.  Since we put an escape character we have \\\\\_italicize\_ and don't need to escape the second underscore since there's not another non-escaped underscore with which to italicize something in between them.  So technically you could have written ¯\\\\\\\\\\\\\\_(ツ)\\\\\_/¯ but you don't need to since there's not a second non-escaped underscore.  You ***would*** need to escape the second underscore if you planned on using another underscore in the same line (but not if you used a line break, aka pressed enter twice).  If you used an asterisk later though on the same line it would not work with the non-escaped underscore to italicize.  To show you this, you can type _italicize* and it should not be italicized."""

#Main function which divides the comments and finds one to reply to
def run_bot(): 
	cache = [reply]
	sub = r.get_subreddit('all')
	comments = sub.get_comments(limit = 100)
	for c in comments:
		if shrug(c) and c.id not in cache and c not in cache:
			c.reply(reply)
			cache.append(c.id)

#Decides if the bot should reply based on each word in the comment
def shrug(c):
	text = c.body
	tokens = text.split()
	if "¯\_(ツ)_/¯" in tokens:
		return True

if __name__ == '__main__':
	while True:
		try:
			run_bot()
			time.sleep(30)
			o.refresh(force=True)
		except (praw.errors.HTTPException, ConnectionError, praw.errors.Forbidden, ConnectionResetError, praw.errors.InvalidComment) as e:
			time.sleep(30)
			o.refresh(force=True)