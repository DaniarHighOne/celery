from django.http import HttpResponse
from . import tasks
# Create your views here.


def home(request):
    tasks.download_cat.delay()
    #task start to perform
    return HttpResponse('<h1>Download a cat</h1>')