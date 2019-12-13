# from requests_oauthlib import OAuth1Session
import os
import dotenv
dotenv.load_dotenv('.env')

TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

# session = OAuth1Session(TWITTER_CONSUMER_KEY,
                        # client_secret=TWITTER_CONSUMER_KEY,
                        # resource_owner_key=TWITTER_ACCESS_TOKEN,
                        # resource_owner_secret=TWITTER_ACCESS_TOKEN_SECRET)

# The URL endpoint to update a status (i.e. tweet)
url = 'https://api.twitter.com/1.1/statuses/update.json'

# The contents of status (i.e. tweet text)
status = 'If you are reading this on Twitter, the API request worked!'

# Send a POST request to the url with a 'status' parameter
# resp = session.post(url, {'status': status})

# Show the text from the response
# print(resp.text)

# print(os.environ)
