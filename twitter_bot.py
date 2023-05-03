import tweepy
import time

# Para ter o acesso do twitter precisamos ter a chave de acesso que conseguimos com a conta de desenvolvedor twitter:
auth = tweepy.OAuthHandler('API KEY', 'API KEY SECRET')
# Acessando twitter
auth.set_access_token('Access Token',
                      'Access Token SECRET')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# bot de twitter que curti os primeiros 2 tweets que encontra que contenha a palavra da variavel search_string.
search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# Bot Generoso que segui de volta seguidores do twiter
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'name of the follower(nome do seguidor)':
#         follower.follow()
#         break

# imprimindo quantidade de seguidores.
# print(user.followers_count)

# Imprimindo twets recentes.
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
