from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.urls import reverse
import logging
from .models import Post, AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactFrom

# Create your views here.


def index(request):

    blog_title ='Latest Post'
    all_posts = Post.objects.all() 

    paginator = Paginator(all_posts, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {'blog_title' : blog_title, 'page_obj' : page_obj})

def details(request, slug):

    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("Page Not Exist")
    
    return render(request, 'blog/detail.html', {'post':post, 'related_posts':related_posts})

def contact(request):
    if request.method == 'POST':

        form = ContactFrom(request.POST)

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")

        if form.is_valid():
            logger.debug(f'POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')

            success_message = "You Submited Successfully"
            return render(request, 'blog/contact.html', {'form':form, 'success_message':success_message})   

        else:
            logger.debug("Form Validation Error")

        return render(request, 'blog/contact.html', {'form':form, 'name':name, 'email':email, 'message':message})   
 
    return render(request, 'blog/contact.html')   

def about(request):

    about_content = AboutUs.objects.first().content
    return render(request, 'blog/about.html', {'about_content':about_content})

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_redirect(request):
    return HttpResponse("This is Redirect New url")

