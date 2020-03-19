from django.shortcuts import render
from movies.models import Movies
# Create your views here.

def index(request):

    movies=Movies.objects.all()
    return render(request,'index.html',{'movies':movies})

