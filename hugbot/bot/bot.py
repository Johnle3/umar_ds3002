import tweepy
import time
import random

consumer_key = 'ky7GT1xmKefU7ZPVD4bmLzGTQ'
consumer_secret = 'y9SRlhYtpt0fHaXbaWrlE35lcz0DChUhGWU8GM82lYqiVwff8e'
access_token = '1522410951143796737-yyHMOTKV4xZnreEe0XVRci3ORC70jz'
access_token_secret = 'NaS5dKC9Er8nbU2Socj9oULGWjZ8JcezVwx6aMuuW8oFm'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

FILE_NAME = 'last.txt'
GIF = 'hug.gif'
help_image = 'help.png'

api = tweepy.API(auth)

# This function will open the text file and return the ID of
# the latest tweet the bot has successfully replied to
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

# Overwrite the previous Tweet ID with latest
def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

appreciations = [
    "You're looking absolutely gorgeous today ;)",
    "Here's a bonus hug from me!",
    "Go drink some water!",
    "I love your tweets!",
    "You're awesome",
    "Should I be worried that my creator is a dumbass?",
    "You're are so smart, people had to increase range of the IQ scale",
    "I want to be as cool as you",
    "Do you want to go out on a coffee date maybe?",
]


# Pick appreciation randomly
def random_appreciation():
    return appreciations[random.randrange(0, 8)]

def reply():
    # The API will only send a response containing tweets with IDs that come after the ID
    # stored in the text file
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#hug' in tweet.full_text.lower():
            print("Hugged!: " + str(tweet.id) + " - " + tweet.full_text.lower())
            api.update_with_media(GIF, "@"+ tweet.user.screen_name + " hug hug" + "\nPS: " + random_appreciation(), in_reply_to_status_id=tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

        if '#help' in tweet.full_text.lower():
            print("Suggested!: " + str(tweet.id) + " - " + tweet.full_text.lower())
            api.update_with_media(help_image, "@"+ tweet.user.screen_name + " use the #hug tag", in_reply_to_status_id=tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

        if '@Hug_Bot_3002' == tweet.full_text.lower().strip() or '.@Hug_Bot_3002' == tweet.full_text.lower().strip():
            print("Suggested!: " + str(tweet.id) + " - " + tweet.full_text.lower())
            api.update_status("Hey @"+ tweet.user.screen_name + "! Use #hug to get a hug", in_reply_to_status_id=tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

        if '#hug' not in tweet.full_text.lower():
            print("Liked!: " + str(tweet.id) + " - " + tweet.full_text.lower())
            store_last_seen(FILE_NAME, tweet.id)

        api.create_favorite(tweet.id) # Like the tweet with mentions


"""
The program needs to run continuously to fetch and reply to tweets. This loop
runs infinitely and executes the reply() functions checking for mentions and
has a timeout of 15 seconds between each poll so that rate limits imposed by
Twitter APIs are not tripped.
"""
while True:
    reply()
    time.sleep(15)