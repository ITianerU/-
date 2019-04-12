from django.shortcuts import render
from django.http import JsonResponse
from functools import reduce
from django.utils.timezone import now
import json
# Create your views here.


def add(request):
    if request.method == "POST":
        value_array = json.loads(request.body.decode())["value_array"]
        result = reduce(lambda x, y: x + y["value"], value_array, 0)
        return JsonResponse({"result": result})

def get_date(request):
    if request.method == "GET":
        return JsonResponse({"date": now().date()})

def chat(request):
    if request.method == "POST":
        result = ""
        msg = json.loads(request.body.decode())["msg"]
        if "您好" in msg and "再见" in msg:
            result = "“天气不错。"
        elif "您好" in msg:
            result = "您好，您吃了吗？"
        elif "再见" in msg:
            result = "回见了您内。"
        return JsonResponse({"result": result}, json_dumps_params={'ensure_ascii': False})

