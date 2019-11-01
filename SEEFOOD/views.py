from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import requests


# Create your views here.
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        data = request.FILES['source']
        ## send the file to /process
        result = requests.get('http://127.0.0.1:8000/',files = {'source':data})
       
        # HTTPclien.sendRequest('http://seefoodapp/image-recg', file)
        # HTTPclien.sendRequest('http://localhost:8000/processs', file)
        return HttpResponse('success/', result)
    else:
        return HttpResponse('Not handled')
    

def save(request):
     if request.method == 'POST':
        file = request.FILES['source']
        file_save = default_storage.save('img', file)
        return HttpResponse('success/')
