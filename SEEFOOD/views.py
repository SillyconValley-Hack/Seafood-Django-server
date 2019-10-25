from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage


# Create your views here.
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        file = request.FILES['source']
        ## send the file to /process
        # HTTPclien.sendRequest('http://seefoodapp/image-recg', file);
        return HttpResponse('success/')
def process(request):
     if request.method == 'POST':
        file = request.FILES['source']
        file_save = default_storage.save('img', file)
        return HttpResponse('success/')
