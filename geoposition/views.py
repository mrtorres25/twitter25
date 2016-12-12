from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import tweepy
from django.core.context_processors import csrf
from tweepy.error import TweepError
from django.contrib.auth.decorators import login_required
import requests
from shutil import copyfile

consumer_key = "CCVw7yjUE0oMAXWfLlar2lgqa"
consumer_secret = "zWko5Oqg32elKUrOiji49yC9LqqoGfKXl5IV6ij7dByIEYuRKJ"

access_token = "15037577-sjnuYAPJeZz56QNCPUpG2NT2Ay7HW4n4Ip50E0z9Y"
access_token_secret = "4xwgzze0mFRpAzu9Lc4PD2BtlNz67mlEqjWCoEJe7k7Pd"

@login_required(login_url='/login/')
def index(request):
    copyfile('media/blank.png','media/map.png')
    return render(request, 'geoposition/index.html',{'user':""})

@login_required(login_url='/login/')
def get_geoposition(request):
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
            copyfile('media/blank.png','media/map.png')
            return render(request, 'geoposition/index.html', {'msg' : "Invalid URL or tweet ID, try again.",'user':""})
        coordinates = getTweetCoordinates(tweet)
        location = getTweetLocation(tweet)
        if(coordinates=="" and location!=""):
            coordinates = getTweetPlace(tweet)
        else:
            coordinates = "No coordinates available."
        rtscoordinates = getRetweetsCoordinates(getStatusId(url),api)
        text = getTweetText(tweet)
        user = getTweetUser(tweet)
        if(coordinates!="No coordinates available."):
            #http://maps.google.com/maps/api/staticmap?center=37.8654938,-4.7791247&zoom=14&size=512x512&maptype=roadmap&markers=color:blue|label:M|37.8654938,-4.7791247&sensor=false
            msg = "http://maps.google.com/maps/api/staticmap?center="+coordinates+"&zoom=4&size=1024x1024&maptype=roadmap&markers=color:blue|"+coordinates
            for coord in rtscoordinates:
                msg += "&markers="+coord
            msg = msg + "&sensor=false"

            if (len(rtscoordinates)==0):
                rtscoordinates = ["None"]

            proxies = {}
            session = requests.Session()
            session.proxies = proxies
            r = session.get(msg)
            f = open('media/map.png','wb')
            f.write(r.content)
            f.close()
            msg=""

            context = {
                'msg' : msg,
                'user' : user,
                'coordinates' : coordinates,
                'text' : text,
                'rtscoordinates' : rtscoordinates
            }
            #print(getRetweetsLocation(getStatusId(url),api))
            return render(request, 'geoposition/index.html', context)
        else:
            copyfile('media/blank.png','media/map.png')
            return render(request, 'geoposition/index.html', {'msg':"No location available.",'user':""})

    else:
        copyfile('media/blank.png','media/map.png')
        return render(request, 'geoposition/index.html', {'msg' : "Empty URL, enter a valid URL.",'user':""})

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

def getRetweetsCoordinates(id, api):
    retweeters = api.retweeters(id)
    locations = []
    i = 0
    for user in retweeters:
        print(i)
        i = i+1
        currentuser = api.get_user(user)
        if (currentuser.status) is not None:
            currentlocation = getTweetPlace(currentuser.status)
            if(currentlocation!=""):
                locations.append(currentlocation)

    print(locations)
    return locations
