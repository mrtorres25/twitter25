from django.shortcuts import render, redirect
from .forms import UrlForm
from django.http import HttpResponseRedirect
import tweepy
from django.core.context_processors import csrf

consumer_key = "CCVw7yjUE0oMAXWfLlar2lgqa"
consumer_secret = "zWko5Oqg32elKUrOiji49yC9LqqoGfKXl5IV6ij7dByIEYuRKJ"

access_token = "15037577-sjnuYAPJeZz56QNCPUpG2NT2Ay7HW4n4Ip50E0z9Y"
access_token_secret = "4xwgzze0mFRpAzu9Lc4PD2BtlNz67mlEqjWCoEJe7k7Pd"

def index(request):
    print("arsaaa")
    return render(request, 'location/index.html')

def get_location(request):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    url = request.GET.get('url')
    url = url.replace("%3A",":")
    url = url.replace("%2F","/")
    print("oleeee oleee")
    tweet = api.get_status(getStatusId(url))
    location = getTweetLocation(tweet)
    place = getTweetPlace(tweet)
    text = getTweetText(tweet)
    user = getTweetUser(tweet)
    context = {
        'location' : location,
        'places' : place,
        'text' : text,
        'user' : user,
        'url' : url
    }
    return render(request, 'location/index.html', context)

def getStatusId(url):
    idx = url.rfind('/')
    id = url[idx+1:]
    return id

def getTweetUser(tweet):
    return tweet.user.name + " | " + tweet.user.screen_name

def getTweetText(tweet):
    return tweet.text

def getTweetPlace(tweet):
    if (tweet.place) is not None:
        loc = tweet.place.name + ", " + tweet.place.country
        print(loc)
        # geocode_result = gmaps.geocode(loc)
        # print(geocode_result)
        # lat = geocode_result[0]["geometry"]["location"]["lat"]
        # lon = geocode_result[0]["geometry"]["location"]["lng"]
        lon = tweet.place.bounding_box.coordinates[0][0][0]
        lat = tweet.place.bounding_box.coordinates[0][0][1]
        returnstr = str(lat) + "," + str(lon)

    else:
        returnstr = "No place available."

    return returnstr

def getTweetLocation(tweet):

    if (tweet.coordinates) is not None:
        coords = tweet.coordinates
        lon = coords["coordinates"][0]
        lat = coords["coordinates"][1]
        returnstr = str(lat) + "," + str(lon)
        print(returnstr)

    else:
        returnstr = "No coordinates available."
        print("No location available.")

    return returnstr
