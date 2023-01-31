from django.urls import path
from . import views


app_name = 'challendge'
 
urlpatterns = [
	path('', views.index, name='index'),
	path('challendge/', views.challendge, name='challendge'),
	# path('challendge/<str:name_challendge>/', views.challendge_one, name='challendge'),
	# path('leaderboard/', views.leaderboard, name='leaderboard'),
	# path('subscribe/', views.subscribe, name='subscribe'),
	# path('resources/', views.resources, name='resources'),
	# path('account/', views.account, name='account'),
	# path('contact/', views.contact, name='contact'),
]
	