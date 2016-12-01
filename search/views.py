from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from tweepy import API
from tweepy import OAuthHandler


def tweet_list(request):

    return render(request, 'search/tweet_list.html', {'errorcode':-1,'message':"Introduzca el texto a buscar"})


def get_queryset(request):
    auth = OAuthHandler('wbSKrzlEya3UJgBzkIkSEkz3F',
                        '5GXAfWSO99HZ2QFhEihb4NF4y9lTvIaCt80mvpUCTr2kMha9Fi')
    auth.set_access_token('800728740082765824-MEGhu5oDdSajvFKtcS3jcMrb8rmEkGq',
                          'RxJYOFORpm3CMX8BwCW6o5ckJ0q1TwaVfa0n3eUeAoLnR')
    api = API(auth,proxy='proxy.lcc.uma.es:3128')
    tosearch=request.GET['q']
    error=0
    message="Hola"
    results=""
    if (tosearch and tosearch.strip()):
        results = api.search(tosearch,count=100)
        # for result in results:
        #   print(result)
        message="Se ha realizado correctamente su busqueda de: \""+tosearch+"\""
    else:
        error=1
        message="No se puede realizar la busqueda de: \""+tosearch+"\""

    context = {
        'result_with_text': results,
        'errorcode':error,
        'message':message
               }
    return render(request, 'search/tweet_list.html', context)
