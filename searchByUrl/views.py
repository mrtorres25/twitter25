from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tweepy import API
from tweepy import OAuthHandler
import  requests as r
import json


@login_required(login_url='/login/')
def tweet_list(request):
    print ("AQUI")
    return render(request, 'searchByUrl/tweet_list.html', {'errorcode':-1,'message':"Introduzca la URL del Tweet"})

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
    tweetembed=""
    if (tosearch and tosearch.strip()):
        try:
            # embed=tosearch.split("?")[0].replace("/","%2F").replace(":","%3A")
            # # print(tosearch.replace("/","%2F"))
            # # print(tosearch.replace(":","%3A"))
            # # print(embed)
            # # print(requests.get("https://publish.twitter.com/oembed",url=embed))
            # # response=r.get("https://publish.twitter.com/oembed?url=https://twitter.com/realmadrid/status/806502275686481928")
            # response = r.get("https://publish.twitter.com/oembed?url="+embed)
            # j=json.dumps(response.json())
            # print()
            # # j=json.load(response.json())
            # # print(j['html'])
            # tweetembed=json.loads(j.replace("\'","\""))['html']
            # # print(json.load(tweetembed)['html'])
            # # print(json.load(r.get("https://publish.twitter.com/oembed?url="+embed).json()))
            # print("HOLA")
            idTweet=tosearch.split("/")[5].split("?")[0]
            results = api.get_status(idTweet)
            print(results)
            message = "Se ha realizado correctamente su busqueda del tweet con url: \"" + tosearch + "\""
        except:
            error=1
            message = "La URL: \"" + tosearch + "\" introducida no es válida"

    else:
        error=1
        message="No se puede realizar la busqueda del tweet con url: \""+tosearch+"\""

    context = {
        'result_with_text': results,
        'errorcode':error,
        'message':message,
        'jsonhtml':tweetembed
               }

    return render(request, 'searchByUrl/tweet_list.html', context)

@login_required(login_url='/login/')
def get_querysetbyid(request):
    auth = OAuthHandler('wbSKrzlEya3UJgBzkIkSEkz3F',
                        '5GXAfWSO99HZ2QFhEihb4NF4y9lTvIaCt80mvpUCTr2kMha9Fi')
    auth.set_access_token('800728740082765824-MEGhu5oDdSajvFKtcS3jcMrb8rmEkGq',
                          'RxJYOFORpm3CMX8BwCW6o5ckJ0q1TwaVfa0n3eUeAoLnR')
    api = API(auth, proxy='proxy.wifi.uma.es:3128')
    tosearch=request.GET['q']
    error=0
    message=""
    results=""
    tweetembed=""
    if (tosearch and tosearch.strip()):
        try:
            embed=tosearch.split("?")[0].replace("/","%2F").replace(":","%3A")
            # print(tosearch.replace("/","%2F"))
            # print(tosearch.replace(":","%3A"))
            print(embed)
            # print(requests.get("https://publish.twitter.com/oembed",url=embed))
            # response=r.get("https://publish.twitter.com/oembed?url=https://twitter.com/realmadrid/status/806502275686481928")
            response = r.get("https://publish.twitter.com/oembed?url="+embed,proxies={'https': 'https://proxy.wifi.uma.es:3128'})
            j=json.dumps(response.json())
            print("AQUIJSON")
            # j=json.load(response.json())
            # print(j['html'])
            tweetembed=json.loads(j.replace("\'","\""))['html']
            # print(json.load(tweetembed)['html'])
            # print(json.load(r.get("https://publish.twitter.com/oembed?url="+embed).json()))
            print("HOLA")
            idTweet=tosearch.split("/")[5].split("?")[0]
            print(idTweet)
            results = api.get_status(idTweet)
            print(results)
            message = "Se ha realizado correctamente su busqueda del tweet con url: \"" + tosearch + "\""
        except:
            error=1
            message = "La URL: \"" + tosearch + "\" introducida no es válida"

    else:
        error=1
        message="No se puede realizar la busqueda del tweet con url: \""+tosearch+"\""

    context = {
        'result_with_text': results,
        'errorcode':error,
        'message':message,
        'jsonhtml':tweetembed
               }

    return render(request, 'searchByUrl/tweet_list.html', context)
