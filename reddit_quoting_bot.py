import praw
from praw.models import MoreComments
import random

#MD5 hash
reddit = praw.Reddit(
    client_id ="1691811324bc8a57a135e00041ae58df",
    client_secret ="730298ea3e1a319c5133275041413020",
    user_agent ="myquotingscript:v1.0",
    username="eb27d8d69905db222b5461ea01688116",
    password="ac4e4e0c328571fb97d3bb45d3e54284",
)

# Selecting a particular subreddit;
subreddit = reddit.subreddit("television")

# Choosing either new/hot/top submissions and how many submissions to traverse;
new_submissions = subreddit.hot(limit=100)

# The phrase to find;
phrase = "the wire"

# A function to check if the bot have already replied to this thread. Only one reply per thread;
# The id's of the submissions that the bot had replied to is stored in plain text file in the same directory;
def check_if_already_replied(id):
    file = open("replied_threads.txt", "r")
    for line in file:
        if id in line:
            file.close()
            return True
    file.close()
    return False

# Add the id of the submission/thread after replying;
def add_to_replied(id):
    file = open("replied_threads.txt", "a")
    file.write(f"{id}\n")
    file.close()
    return

quotes = [
	"A man must have a code. - Omar Little",
	"You come at the king, you best not miss. — Omar Little",
	"How you expect to run with the wolves come night, when you spend all day sparring with the puppies? - Omar Little",
	"Man, money ain't got no owners. Only spenders. — Omar Little",
	"All in the game, yo... All in the game. - Omar Little",
	"Look man, I do what I can do to help y’all. But the game is out there, and it’s either play or get played. - Omar Little",
	"The bigger the lie, the more they believe. - William 'Bunk' Moooreland",
	"The Bunk can’t swim. I ain’t too good at floating, either. - William 'Bunk' Moooreland",
	"I feel like I don't even belong to any world that even f****** matters. — Jimmy McNulty",
	"You play in dirt, you get dirty. - Jimmy McNulty",
	"There are no f****** rules. F****** game is rigged. - Jimmy McNulty",
	"I caught him, Bunk. On the wire. I caught him. And he doesn’t f***ing know it. - Jimmy McNulty",
	"Well, you know what they say: ‘stupid criminal make stupid cops.’ I’m proud to be chasing this guy. — Jimmy McNulty",
	"I don't wanna go to no dance unless I can rub some t**. — Lester Freamon",
	"A life, Jimmy, you know what that is? It’s the s*** that happens while you’re waiting for moments that never come. - Lester Freamon",
	"You follow drugs, you get drug addicts and drug dealers. But you start to follow the money, and you don’t know where the f*** it’s gonna take you. — Lester Freamon",
	"We’re building something, here, detective. We’re building it from scratch. All the pieces matter. — Lester Freamon",
	"If that idiot worked for us, he’d be a deputy commissioner by now. - Roland 'Prez' Pryzbylewski",
	"No one wins. One side just loses more slowly. - Roland 'Prez' Pryzbylewski",
	"Cases gotta go green before they go black. - Shakima 'Kima' Greggs",
	"You'd rather live in shit than let the world see you work a shovel. — Cedric Daniels",
	"The game is rigged, but you cannot lose if you do not play. — Marla Daniels",
	"Middle management means that you have just enough responsibility that you got to listen when people talk, and not so much that you can tell anybody to go f*** themselves. - Howard 'Bunny' Colvin",
	"I want to see you land okay, Jimmy. So, tell me, where don’t you wanna go? - William Rawls",
	"Crawl, walk, and then run. - R. Clayton 'Clay' Davis",
	"You think I have time to ask a man why he giving me money? Or where he gets his money from? I’ll take any m************ money if he giving it away! - R. Clayton 'Clay' Davis",
	"The past is always with us. And where we come from, what we go through, how we go through it, all that s*** matters. - D'Angelo Barksdale",
	"You know the difference between me and you? I bleed red and you bleed green. — Avon Barksdale",
	"This here game is more than the rep you carry, the corner you hold. You gotta be fierce, I know that. But more than that, you gotta show some flex. Give and take on both sides. - Russell 'Stringer' Bell",
	"It ain’t easy civilizing this m***********. - Joseph 'Proposition Joe' Stewart",
	"Stir up a hornet’s nest, ain’t no telling who’s gonna get stung. - Joseph 'Proposition Joe' Stewart",
	"Wanna know what kills more police than bullets and liquor? Boredom. They just can't handle that s***. — Joseph 'Proposition Joe' Stewart",
	"Lambs go to slaughter. A man, he learns when to walk away. — The Greek",
	"Business. Always business. - The Greek",
	"You trust a man, you stay with him. - Spiros 'Vondas' Vondopoulos",
	"We used to make s*** in this country, build s***. Now we just put our hand in the next guy's pocket. — Frank Sobotka",
	"This game is rigged, man. We like the little b****** on a chessboard. - Preston 'Bodie' Broadus",		
	"Yeah now, well, the thing about the old days... they the old days. — Slim Charles",
	"Ain’t no shame in holding on to grief. As long as you make room for other things, too. - Reginald 'Bubbles' Cousins",
]

def get_random_quote():
	random_number = random.randint(0, len(quotes)-1)
	return quotes[random_number]

# Bot is scanning the comments and replies tree;
# At this time the bot is ran manually by running the program;
# Only one reply at a time;
def main():
    for submission in new_submissions:
        for comment in submission.comments:
            if isinstance(comment, MoreComments): #Addressing AttributeError: 'MoreComments' object has no attribute 'body' exception;
                continue
            if phrase in comment.body.lower():
                if not check_if_already_replied(submission.id):
                    comment.reply(f"The wire is a great show!\n\n {get_random_quote()}")
                    add_to_replied(submission.id)
                    return
            for reply in comment.replies:
                if isinstance(reply, MoreComments):
                    continue
                if phrase in reply.body.lower():
                    if not check_if_already_replied(submission.id):
                        reply.reply(f"The wire is a great show!\n\n {get_random_quote()}")
                        add_to_replied(submission.id)
                        print(submission.title)
                        return

main()



