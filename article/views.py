from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from article.models import Tag
from datetime import datetime
from django.http import Http404

# Create your views here.
def home(request):
    #return HttpResponse("Hello World, Django")
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list' : post_list})
"""
def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s"
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
    #return HttpResponse("You're looking at my_args %s." % my_args)
"""

def test(request):
    return render(request, 'test.html',{'current_time': datetime.now()})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
        tags = post.tag.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post, 'tags': tags})

def about_me(request) :
    return render(request, 'aboutme.html')
def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoseNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list':post_list, 'error':False})

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')