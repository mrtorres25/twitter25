from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.shortcuts import render
from django.conf import settings
from tweepy import API
from tweepy import OAuthHandler
import json
import  requests as r

@login_required(login_url='/login/')
def tweet_list(request):
    return render(request, 'searchUser/tweet_list.html', {'errorcode':-1,'message':"Introduzca el texto a buscar"})

@login_required(login_url='/login/')
def get_queryset(request):
    auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    api = API(auth)
    tosearch=request.GET['q']
    error=0
    message=""
    results=""
    followers=""
    if (tosearch and tosearch.strip()):
        try:
            # print(tosearch)
            results = api.get_user(screen_name=tosearch)
            # print(results)
            followers=api.followers(id=results.id)
            # print(results)
            print(followers)
            message = "Se ha realizado correctamente su busqueda de: \""+tosearch+"\""
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
        'followers':followers,
               }
    return render(request, 'searchUser/tweet_list.html', context)