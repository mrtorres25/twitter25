# Create your views here.

from django.shortcuts import render
from tweepy import API
from tweepy import OAuthHandler


def tweet_list(request):
    print ("AQUI")
    return render(request, 'searchByUrl/tweet_list.html', {'errorcode':-1,'message':"Introduzca la URL d"})


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
        # country=api.reverse_geocode(lat=40.447269,long=-3.691702,granularity='country')
        # print(api.reverse_geocode(lat=40.447269,long=-3.691702,granularity='country'))
        # for c in country:
        # print(api.get_status('805709551337086980'))
        # countryid=country[0].id
        # print(countryid)
        # for string in tosearch.split("/"):
        #     print(string)
        idTweet=tosearch.split("/")[5].split("?")[0]
        # print(idTweet)
        results = api.get_status(idTweet)
        # for result in results:
        #   print(result)
        print(results)
        message="Se ha realizado correctamente su busqueda del tweet con url: \""+tosearch+"\""
    else:
        error=1
        message="No se puede realizar la busqueda del tweet con url: \""+tosearch+"\""

    context = {
        'result_with_text': results,
        'errorcode':error,
        'message':message
               }
    return render(request, 'searchByUrl/tweet_list.html', context)
