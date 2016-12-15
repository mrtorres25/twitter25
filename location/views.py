from django.shortcuts import render, redirect
from .forms import UrlForm
from django.http import HttpResponseRedirect
import tweepy
from django.core.context_processors import csrf
from tweepy.error import TweepError
from django.contrib.auth.decorators import login_required

consumer_key = "CCVw7yjUE0oMAXWfLlar2lgqa"
consumer_secret = "zWko5Oqg32elKUrOiji49yC9LqqoGfKXl5IV6ij7dByIEYuRKJ"

access_token = "15037577-sjnuYAPJeZz56QNCPUpG2NT2Ay7HW4n4Ip50E0z9Y"
access_token_secret = "4xwgzze0mFRpAzu9Lc4PD2BtlNz67mlEqjWCoEJe7k7Pd"

@login_required(login_url='/login/')
def index(request):
    return render(request, 'location/index.html',{'user':""})

@login_required(login_url='/login/')
def get_location(request):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,proxy="proxy.wifi.uma.es:3128")
    url = request.GET.get('url')
    if((url is not None) and (url!="")):
        url = url.replace("%3A",":")
        url = url.replace("%2F","/")
        try:
            tweet = api.get_status(getStatusId(url))
        except TweepError:
            return render(request, 'location/index.html', {'user' : "Invalid URL or tweet ID, try again."})
        coordinates = getTweetCoordinates(tweet)
        location = getTweetLocation(tweet)
        if(coordinates=="" and location!=""):
            coordinates = getTweetPlace(tweet)
        else:
            coordinates = "No coordinates available."
        if(location==""):
            location = "No location available."
        text = getTweetText(tweet)
        user = getTweetUser(tweet)
        retweets = getRetweetAmount(tweet)
        rtslocation = getRetweetsLocation(getStatusId(url),api)
        if (len(rtslocation)==0):
            rtslocation = ["None"]
        context = {
            'coordinates' : coordinates,
            'location' : location,
            'text' : text,
            'user' : user,
            'url' : url,
            'rts' : retweets,
            'rtslocation' : rtslocation
        }
        #print(getRetweetsLocation(getStatusId(url),api))
        return render(request, 'location/index.html', context)

    else:
        return render(request, 'location/index.html', {'user' : "Empty URL, enter a valid URL."})

def getStatusId(url):
    idx = url.rfind('/')
    id = url[idx+1:]
    return id

def getRetweetAmount(tweet):
    return tweet.retweet_count

def getTweetUser(tweet):
    return tweet.user.name + " | @" + tweet.user.screen_name

def getTweetText(tweet):
    return tweet.text

def getTweetLocation(tweet):
    if(tweet.place) is not None:
        returnstr = tweet.place.name + ", "+ tweet.place.country
    else:
        returnstr = ""
    return returnstr

def getTweetPlace(tweet):
    if (tweet.place) is not None:
        # geocode_result = gmaps.geocode(loc)
        # print(geocode_result)
        # lat = geocode_result[0]["geometry"]["location"]["lat"]
        # lon = geocode_result[0]["geometry"]["location"]["lng"]
        lon = tweet.place.bounding_box.coordinates[0][0][0]
        lat = tweet.place.bounding_box.coordinates[0][0][1]
        returnstr = str(lat) + ", " + str(lon)

    else:
        returnstr = ""

    return returnstr

def getTweetCoordinates(tweet):

    if (tweet.coordinates) is not None:
        coords = tweet.coordinates
        lon = coords["coordinates"][0]
        lat = coords["coordinates"][1]
        returnstr = str(lat) + ", " + str(lon)
        print(returnstr)

    else:
        returnstr = ""
        print("No location available.")

    return returnstr

def getRetweetsLocation(id, api):
    retweeters = api.retweeters(id)
    locations = []
    i = 0
    for user in retweeters:
        print(i)
        i = i+1
        currentuser = api.get_user(user)
        if (currentuser.status) is not None:
            currentlocation = getTweetLocation(currentuser.status)
            if(currentlocation!=""):
                locations.append(currentlocation)

    print(locations)
    return locations
