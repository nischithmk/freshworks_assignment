from django.shortcuts import render,redirect
import json
from django.conf import settings
import redis
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from .forms import SomeForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)

#view for get and post request
@csrf_exempt
def manage_items(request, *args, **kwargs):
    if request.method == 'POST':
        form = SomeForm(request.POST)
        if form.is_valid():
            item=(form.cleaned_data['name'])
            item = eval(item)
            key = list(item.keys())[0]
            value = item[key]
            if redis_instance.exists(key):
                return redirect('failure')
            else:
                redis_instance.set(key, value)
                return redirect('success')
        else:
            form = SomeForm()
            return render(request, 'app1/Home.html')

    return render(request,'app1/Home.html')

#view for post request success message
def success(request):
    return render(request,'app1/success.html')
#view for post request failure message
def failure(request):
    return render(request,'app1/failure.html')

#view for get request
def get_single_key(request):
    if request.method == 'GET':
        keyword = request.GET.get('search')
        value = redis_instance.get(keyword)
        if value:
            data = {'key': keyword,'value': value.decode('utf-8'),'msg': 'success'}
        else:
            data = {'key': keyword,'value': None,'msg': 'Key Not found'}
        return render(request,'app1/Home.html',{"data":data})

#view for delete request
def delete_key(request):
    if request.method == 'GET':
        keyword = request.GET.get('delete')
        result = redis_instance.delete(keyword)
        if result == 1:
            response = {'msg': f"{keyword} successfully deleted"}
        else:
            response = {'key': keyword,'value': None,'msg': 'Key Not found'}
        return render(request,'app1/Home.html',{"response":response})