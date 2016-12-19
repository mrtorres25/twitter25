from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.shortcuts import render
from tweepy import API
from tweepy import OAuthHandler
import json
import  requests as r

@login_required(login_url='/login/')
def tweet_list(request):
    return render(request, 'searchUser/tweet_list.html', {'errorcode':-1,'message':"Introduzca el texto a buscar"})

@login_required(login_url='/login/')
def get_queryset(request):
    auth = OAuthHandler('wbSKrzlEya3UJgBzkIkSEkz3F',
                        '5GXAfWSO99HZ2QFhEihb4NF4y9lTvIaCt80mvpUCTr2kMha9Fi')
    auth.set_access_token('800728740082765824-MEGhu5oDdSajvFKtcS3jcMrb8rmEkGq',
                          'RxJYOFORpm3CMX8BwCW6o5ckJ0q1TwaVfa0n3eUeAoLnR')
    api = API(auth)
    tosearch=request.GET['q']
    error=0
    message=""
    results=""
    if (tosearch and tosearch.strip()):
        try:
            results = api.get_user(tosearch)
            message = "Se ha realizado correctamente su busqueda de: \""+tosearch+"\""
            print (results)
        except:
            error=1
            message = "Ha Ocurrido un error. No se puede realizar la busqueda de: \""+tosearch+"\""
    else:
        error=1
        message="No se puede realizar la busqueda de: \""+tosearch+"\""

    context = {
        'result_with_text': results,
        'errorcode':error,
        'message':message,
               }
    return render(request, 'searchUser/tweet_list.html', context)

def countrycoord(country):
    response = r.get("https://restcountries.eu/rest/v1/alpha/" + country)
    j = response.json()
    print(j['latlng'][0])
    print(j['latlng'][1])

    return (str(j['latlng'][0])+","+str(j['latlng'][1])+",100km")