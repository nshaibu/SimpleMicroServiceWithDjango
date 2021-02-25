import redis
import json

from django.conf import settings
from django.shortcuts import render
from django.http.response import JsonResponse

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


def get_redis(request, key):
    if request.method == 'GET':
        value = redis_instance.get(key)
        return JsonResponse(data={"status": "ok", "value": str(value)})
    return JsonResponse(data={"status": "error", "message": "Method not supported"})
