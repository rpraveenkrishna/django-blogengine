from django.http import HttpResponse
from django.template import Context, RequestContext
from django.core.cache import cache
from django.core import serializers
from hitcounter.models import UserInfo
import settings

def index(request, website_url):
    try:
        cache_value_for_website = cache.get(website_url) 
        
        if cache_value_for_website == None:
            user_info = UserInfo.objects.filter(website_url =  website_url)[0]
            cache.set(user_info.website_address, user_info.hit_counter + 1 )
        else:
            cache.set(user_info.website_address, cache_value_for_website + 1 )
            user_info = UserInfo()
            user_info.hit_counter = cache_value_for_website + 1
            user_info.website_address = website_address
            user_info.website_name = website_address
        
        json_serializer = serializers.get_serializer("json")()
        json_serializer.serialize(user_info, ensure_ascii=False, stream=response)
        
    except Exception, e:
        pass
    
    return json_serializer
