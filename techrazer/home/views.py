from django.shortcuts import render,HttpResponse
from .models import Contact
from home.models import Post
from django.contrib import messages
from django.utils import timezone
import datetime
# Create your views here.
def home(request):

    flts = Post.objects.all().order_by('-timestamp')[0:7]
    slts = Post.objects.all().order_by('-timestamp')[0:4]
    rapidlts = Post.objects.all().order_by('-timestamp')[0:6]

    allPosts = Post.objects.all()
    popularPosts = Post.objects.all().order_by('-views')[0:6]
    
    week_ago = datetime.date.today() - datetime.timedelta(days=10)
    trends = Post.objects.filter(timestamp__gte = week_ago).order_by('-views')[0:6]



    context = {'allPosts': allPosts,'flts':flts,'slts':slts,'rapidlts':rapidlts,'popularPosts':popularPosts,'trends':trends}
    return render(request, "home/home.html",context)

def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    post.views=post.views + 1
    post.save()

    flts = Post.objects.all().order_by('-timestamp')[0:7]
    rapidlts = Post.objects.all().order_by('-timestamp')[0:6]

    popularPosts = Post.objects.all().order_by('-views')[0:6]    
    
    context = {'post':post,'flts':flts,'popularPosts':popularPosts,'rapidlts':rapidlts}
    return render(request , 'home/post.html',context)  

def Category(request,cats):

    category_posts = Post.objects.filter(category=cats).order_by('-timestamp')
    context = {'cats': cats, 'category_posts':category_posts}
    return render(request, 'home/category.html',context)


def search(request):
    query = request.GET['query']
    if len(query)<1:
        allPosts= Post.objects.none() 
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent  = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent).order_by('-published_date')

        if allPosts.count() == 0:
            messages.warning(request, "No results found. Please refine your query!")
    params = {'allPosts' : allPosts, 'query' : query}
    return render(request, "home/search.html", params) 

def contact(request):
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            content = request.POST['content']
            if len(name)<3 or len(email)<5 or len(phone)<6 or len(content)<4:
                messages.error(request, "Please fill form correctly")   
            else:    
                contact =  Contact(name=name , email = email , phone=phone , content=content)
                contact.save()
                messages.success(request, "Your massage has been successfully sent!")
        return render(request, 'home/contact.html')


def privacy(request):
    return render(request, 'home/privacy.html')
def termandconditions(request):
    return render(request, 'home/term&conditions.html')
def disclaimer(request):
    return render(request, 'home/disclaimer.html')