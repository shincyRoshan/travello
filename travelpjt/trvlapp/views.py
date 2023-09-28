from django.shortcuts import render
from . models import places
from . models import TeamMembers
# Create your views here.
def index(request):
    obj = places.objects.all()
    obj2=TeamMembers.objects.all()
    return render(request, "index.html",{'res1':obj,'res2':obj2})
