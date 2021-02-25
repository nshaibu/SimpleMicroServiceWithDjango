import redis
import json

from django.conf import settings
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

@csrf_exempt
def set_redis(request):
    if request.method == 'POST':
        count = 0
        data = request.POST
        for key, value in data.items():
            redis_instance.set(key, value)
            count += 1
        
        return JsonResponse(data={"status": "ok", "count": count})
    return JsonResponse(data={"status": "error", "message": "Method not supported"})
