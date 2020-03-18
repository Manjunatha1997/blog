from django.shortcuts import render
from movies.models import Movies
# Create your views here.

def index(request):

    m1=Movies()
    m1.img="jersy.jpg"
    m1.title="Jersey"
    m1.cast="Nani,Shraddha Srinath"

    m2 = Movies()
    m2.img = "nenu local.jpg"
    m2.title = "Nenu Local"
    m2.cast = "Nani, Keerthi Suresh"

    m3 = Movies()
    m3.img = "gang leader.jpg"
    m3.title = "Gang Leader"
    m3.cast = "Nani, Priyanka "

    m4 = Movies()
    m4.img = "gentleman.jpg"
    m4.title = "Gentleman"
    m4.cast = "Nani, Nivedha "

    movies=[m1,m2,m3,m4]

    return render(request,'index.html',{'movies':movies})

