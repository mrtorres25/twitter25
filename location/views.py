from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import tweepy
from django.core.context_processors import csrf
from django.conf import settings
from tweepy.error import TweepError
from django.contrib.auth.decorators import login_required
import requests
from shutil import copyfile
import json

consumer_key = "CCVw7yjUE0oMAXWfLlar2lgqa"
consumer_secret = "zWko5Oqg32elKUrOiji49yC9LqqoGfKXl5IV6ij7dByIEYuRKJ"

access_token = "15037577-sjnuYAPJeZz56QNCPUpG2NT2Ay7HW4n4Ip50E0z9Y"
access_token_secret = "4xwgzze0mFRpAzu9Lc4PD2BtlNz67mlEqjWCoEJe7k7Pd"

@login_required(login_url='/login/')
def index(request):
    copyfile('media/blank.png','media/map.png')
    return render(request, 'location/index.html',{'username':""})

@login_required(login_url='/login/')
def get_location(request):
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    # api = tweepy.API(auth,proxy="proxy.wifi.uma.es:3128")
    originalurl = request.GET.get('url')
    if((originalurl is not None) and (originalurl!="")):
        url = originalurl.replace("%3A",":").replace("%2F","/")
        try:
            tweet = api.get_status(getStatusId(url))
            results = api.retweets(getStatusId(url))
            embeddedtweet = getEmbeddedTweet(originalurl)
        except TweepError:
            copyfile('media/blank.png','media/map.png')
            return render(request, 'location/index.html', {'msg' : "Invalid URL or tweet ID, try again.",'username':""})
        coordinates = getTweetCoordinates(tweet)
        location = getTweetLocation(tweet)
        if(coordinates=="" and location!=""):
            coordinates = getTweetPlace(tweet)
        else:
            coordinates = "No coordinates available."
        rts = getRetweetsCoordinates(getStatusId(url),api)
        rtscoordinates = rts["locations"]
        rtsplaces = rts["places"]
        text = getTweetText(tweet)
        user = getTweetUser(tweet)

        if(coordinates=="No coordinates available." and len(rtscoordinates)==0):
            copyfile('media/blank.png','media/map.png')
            return render(request, 'location/index.html', {'msg':"No location available.",'username':"",'results':results})
        else:
            if(coordinates!="No coordinates available."):
                msg = "http://maps.google.com/maps/api/staticmap?center="+coordinates+"&zoom=4&size=1024x1024&maptype=roadmap&markers=color:blue|"+coordinates
            else:
                msg = "http://maps.google.com/maps/api/staticmap?center="+rtscoordinates[0]+"&zoom=4&size=1024x1024&maptype=roadmap"

            for coord in rtscoordinates:
                msg += "&markers="+coord
            msg = msg + "&sensor=false"

            mapurl = msg
            msg = ""

            context = {
                'msg' : msg,
                'mapurl' : mapurl,
                'username' : user,
                'coordinates' : coordinates,
                'text' : text,
                'results' : results,
                'rtscoordinates' : rtscoordinates,
                'jsonhtml' : embeddedtweet
            }
            #print(getRetweetsLocation(getStatusId(url),api))
            return render(request, 'location/index.html', context)

    else:
        copyfile('media/blank.png','media/map.png')
        return render(request, 'location/index.html', {'msg' : "Empty URL, enter a valid URL.",'username':""})

def getTweetLocation(tweet):
    if(tweet.place) is not None:
        returnstr = tweet.place.name + ", "+ tweet.place.country
    else:
        returnstr = ""
    return returnstr

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

def getTweetPlace(tweet):
    if (tweet.place) is not None:
        # geocode_result = gmaps.geocode(loc)
        # print(geocode_result)
        # lat = geocode_result[0]["geometry"]["location"]["lat"]
        # lon = geocode_result[0]["geometry"]["location"]["lng"]
        lon = tweet.place.bounding_box.coordinates[0][0][0]
        lat = tweet.place.bounding_box.coordinates[0][0][1]
        returnstr = str(lat) + "," + str(lon)

    else:
        returnstr = ""

    return returnstr

def getTweetCoordinates(tweet):

    if (tweet.coordinates) is not None:
        coords = tweet.coordinates
        lon = coords["coordinates"][0]
        lat = coords["coordinates"][1]
        returnstr = str(lat) + "," + str(lon)
        print(returnstr)

    else:
        returnstr = ""
        print("No location available.")

    return returnstr

def getEmbeddedTweet(url):
    embed = url.replace("/", "%2F").replace(":", "%3A")
    #response = r.get("https://publish.twitter.com/oembed?url=" + embed,proxies={'https': 'https://proxy.wifi.uma.es:3128'})
    j = requests.get("https://publish.twitter.com/oembed?url="+embed).json()
    j = json.dumps(j)
    tweetembed = json.loads(j.replace("\'", "\""))['html']
    return tweetembed

def getRetweetsCoordinates(id, api):
    retweeters = api.retweeters(id)
    locations = []
    places = []
    i = 0
    for user in retweeters:
        print(i)
        i = i+1
        currentuser = api.get_user(user)
        if (currentuser.status) is not None:
            currentlocation = getTweetPlace(currentuser.status)
            if(currentlocation!=""):
                locations.append(currentlocation)
            currentplace = getTweetLocation(currentuser.status)
            if(currentplace!=""):
                places.append(currentplace)

    return {'locations':locations,'places':places}
