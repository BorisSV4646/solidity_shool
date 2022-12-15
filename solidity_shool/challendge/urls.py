from django.urls import path
 
from . import views
app_name = 'logs'
 
urlpatterns = [
	path('', views.index, name='index'),
	path('challendge/', views.challendge, name='challendge'),
	path('challendge/<str:name_challendge>/', views.challendge_one, name='challendge'),
]
