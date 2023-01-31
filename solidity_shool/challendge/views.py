from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'base.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
    }
    return render(request, template, context)

def challendge(request):
    template = 'includes/post.html'
    title = 'Упражнения'
    context = {
        'title': title,
    }
    return render(request, template, context)

def challendge_one(request):
    pass

def leaderboard(request):
    pass

def subscribe(request):
    pass

def resources(request):
    pass

def account(request):
    pass

def contact(request):
    pass
