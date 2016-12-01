import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import googlemaps

consumer_key = "CCVw7yjUE0oMAXWfLlar2lgqa"
consumer_secret = "zWko5Oqg32elKUrOiji49yC9LqqoGfKXl5IV6ij7dByIEYuRKJ"

access_token = "15037577-sjnuYAPJeZz56QNCPUpG2NT2Ay7HW4n4Ip50E0z9Y"
access_token_secret = "4xwgzze0mFRpAzu9Lc4PD2BtlNz67mlEqjWCoEJe7k7Pd"

def getStatusId(url):
    idx = url.rfind('/')
    id = url[idx+1:]
    return id

def getLocation(tweet):
    if (tweet.coordinates) is not None:
        coords = tweet.coordinates
        lon = coords["coordinates"][0]
        lat = coords["coordinates"][1]
        returnstr = str(lat) + "," + str(lon)
        print(returnstr)

    else:
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
            print(returnstr)
        else:
            returnstr = "No location available."
            print("No location available.")

    return returnstr

if __name__ == '__main__':

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    gmaps = googlemaps.Client(key="AIzaSyDXl1-VxlNFMcq0E13ln51D-5rMLxDjrVc")
    api = tweepy.API(auth)
    user = api.me()

    #Tweet con ubicación en Montevideo, Uruguay
    #id = "804123242063609856"
    #Tweet con 10 RT
    #id = "804256400511827969"
    #Tweet con la rehostia de RTs
    #id = "804065897862361088"

    url = "https://twitter.com/Balbonator/status/771499504667426816"
    id = getStatusId(url)
    print(api.get_status(id).text)
    getLocation(api.get_status(id))
    print(api.retweeters(id))
    retweeters = api.retweeters(id)
    for user in retweeters:
        currentuser = api.get_user(user)
        print(currentuser)
        if (currentuser.status) is not None:
            getLocation(currentuser.status)