# from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog

def home(request):
    # return HttpResponse('<h2>Homepage</h2>')
    categories=Category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True).order_by('-updated_at')
    # print(categories)
    # print(featured_posts)
    context={
        'categories':categories,
        'featured_posts':featured_posts,
    }
    return render(request,'home.html',context)