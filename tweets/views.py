from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet


# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1> Hello World </h1>")


def tweet_detail_view(request, tweet_id, *args, **kwargs):

    """
    REST API VIEW
    
    Consume by Javascript or swift/java
    
    return json data
    """

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404

    data = {
        "id": tweet_id,
        "content": obj.content,
        #"image_path":obj.image.url

    }

    return JsonResponse(data, status=status) #json.dumps content_type=(f"<h1> Hello {tweet_id} - {obj.content} </h1>")
