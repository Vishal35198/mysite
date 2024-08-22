
from django.http import HttpResponse
from django.shortcuts import render 

# from django.contrib.auth.model
# we are getting respose error as if though we are doing the project 

def index(request):
    params = {'name':'Vishal','place':'mars'}
    return render(request, 'index.html',params)
#---------------------------------------------------------


def about(request):
    # msg = ""
    # with open('mysite/one.txt','r') as file:
    #     msg =  file.read()
    return HttpResponse("Hello this is the page about")

def getname(request):
    text = request.GET.get('textarea','default')
#--------------------------------------------------------

    return HttpResponse(f" <a href = '/'> {text} <a/>")

def abt(request):
    return HttpResponse("")
