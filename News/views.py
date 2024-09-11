from django.shortcuts import render

from .models import News

def index(request):
	news = News.objects.all()
	return render(request, 'index.html', {'news': news, 'title': 'News list'})