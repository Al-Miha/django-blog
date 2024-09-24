from django.http import HttpResponse
from django.shortcuts import render
# from blogs.models import Blog
from .models import Blog

# Create your views here.

def posts_by_category(request, category_id):
    # print(category_id)
    # return HttpResponse('Posts by category')
    # Fetch the posts that below to category with the id category_id
    posts = Blog.objects.filter(status="Published",category=category_id)
    context={
        'posts':posts,
    }
    return render(request,'posts_by_category.html',context)
