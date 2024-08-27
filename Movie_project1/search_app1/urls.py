from django.urls import path
from. import views

app_name = 'search_app1'
urlpatterns = [
    path('', views.SearchResult, name='SearchResult'),
]