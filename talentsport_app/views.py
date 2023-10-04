from django.shortcuts import render
import requests

def test(request):
    r = requests.get('http://127.0.0.1:8000/disciplines',auth=("super@gmail.com","Dossajunior67."))
    disciplines = r.json()
    print(disciplines)
    context = {'disciplines':disciplines}

    return render(request,"home.html",context)
# Create your views here.
