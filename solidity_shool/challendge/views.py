from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'challendge/index.html'
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
    template = 'base.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
    }
    return render(request, template, context)

def leaderboard(request):
    template = 'base.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
    }
    return render(request, template, context)

def price(request):
    template = 'base.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
    }
    return render(request, template, context)

def resources(request):
    template = 'base.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
    }
    return render(request, template, context)

def account(request):
    template = 'base.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
    }
    return render(request, template, context)

def contact(request):
    template = 'base.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
    }
    return render(request, template, context)
