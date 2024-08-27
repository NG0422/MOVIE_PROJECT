from django.urls import path
from . import views

app_name = 'Movieapp1'
urlpatterns = [

     path('add/', views.add_movie, name='add_movie'),
     path('update/<int:id>/', views.update, name='update'),
     path('delete/<int:id>/', views.delete, name='delete'),

     path('', views.allMovCat,name='allMovCat'),
     path('<slug:c_slug>/', views.allMovCat,name='movies_by_category'),
     path('<slug:c_slug>/<slug:movie_slug>/', views.movDetail,name='movCatdetail'),



]