from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from . models import Category,Movie
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from .forms import MovieForm

# Create your views here.
def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        description = request.POST.get('description', )
        releaseDate = request.POST.get('releaseDate', )
        actors = request.POST.get('actors', )
        category = request.POST.get('category', )
        reviews = request.POST.get('reviews', )
        ratings = request.POST.get('ratings', )
        youtube_url = request.POST.get('youtube_url',)
        img = request.FILES['img']
        movie = Movie(name=name, description=description, releaseDate=releaseDate, actors=actors, category=category, reviews=reviews, ratings=ratings, youtube_url=youtube_url, img=img)
        movie.save()

    return render(request,'add.html')



def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{ 'form':form,'movie':movie })


def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

def allMovCat(request,c_slug=None):
    c_page = None
    movies_list = None
    if c_slug!=None:
        c_page = get_object_or_404(Category, slug=c_slug)
        movies_list = Movie.objects.all().filter(category=c_page, available=True)
    else:
        movies_list = Movie.objects.all().filter(available=True)
    paginator=Paginator(movies_list, 9)
    try:
        page=int(request.Get.get('page', '1'))
    except:
        page = 1
    try:
        movies = paginator.page(page)
    except (EmptyPage, InvalidPage):
        movies = paginator.page(paginator.num_pages)

    return render(request, "category.html", {'category': c_page, 'movies': movies})

def movDetail(request,c_slug,movie_slug):
    try:
        movie = Movie.objects.get(category__slug=c_slug, slug=movie_slug)
    except Exception as e:
        raise e
    return render(request, 'movie.html', {'movie': movie})


