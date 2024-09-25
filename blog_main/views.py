# from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog
from assignments.models import About
from .forms import RegistrationForm


def home(request):
    # return HttpResponse('<h2>Homepage</h2>')
    #  !!! Categorie are now availble through context_processors !!!
    # categories=Category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at')
    # print(categories)
    # print(featured_posts)
    posts=Blog.objects.filter(is_featured=False,status='Published')
    # print(posts)
    about= About.objects.get(pk=1)


    context={
        # 'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts,
        'about':about,
    }
    return render(request,'home.html',context)

def register(request):
    form = RegistrationForm()

    context = {
        'form': form,
    }

    return render(request,'register.html', context)