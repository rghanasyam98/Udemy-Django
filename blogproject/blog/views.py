from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from datetime import date

from django.urls import reverse
from .models import Post,Author,Tag
from . forms import CommentForm
from django.views.generic import ListView,DetailView
from django.views import View

# Create your views here.


allposts=[
    {
        "slug":"gjjsdhdlldshlk",
        "image":"mountains.jpg",
        "author":"ajhfjkgskj",
        "date": date(1998,7,19),
        "title":"stbsbs",
        "excerpt":"jdhaheoifnkf",
        "content":""" Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam, cum alias. Dicta officiis cupiditate laborum temporibus molestias. Doloribus earum dolore aspernatur doloremque eum aperiam neque debitis. Reiciendis, doloremque voluptatibus! Ducimus.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam, cum alias. Dicta officiis cupiditate laborum temporibus molestias. Doloribus earum dolore aspernatur doloremque eum aperiam neque debitis. Reiciendis, doloremque voluptatibus! Ducimus.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam, cum alias. Dicta officiis cupiditate laborum temporibus molestias. Doloribus earum dolore aspernatur doloremque eum aperiam neque debitis. Reiciendis, doloremque voluptatibus! Ducimus.
        """
    },
    {
        "slug":"fdgsrrgsv",
        "image":"woods.jpg",
        "author":"ajhfjkgskj",
        "date": date(1998,7,20),
        "title":"fsetvesv",
        "excerpt":"jdhaheoifnkf",
        "content":""" Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam, cum alias. Dicta officiis cupiditate laborum temporibus molestias. Doloribus earum dolore aspernatur doloremque eum aperiam neque debitis. Reiciendis, doloremque voluptatibus! Ducimus.
          
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam, cum alias. Dicta officiis cupiditate laborum temporibus molestias. Doloribus earum dolore aspernatur doloremque eum aperiam neque debitis. Reiciendis, doloremque voluptatibus! Ducimus.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam, cum alias. Dicta officiis cupiditate laborum temporibus molestias. Doloribus earum dolore aspernatur doloremque eum aperiam neque debitis. Reiciendis, doloremque voluptatibus! Ducimus.
        """
    },
    {
        "slug":"title-3",
        "image":"max.png",
        "author":"ajhfjkgskj",
        "date": date(1998,7,21),
        "title":"jfhjhafan",
        "excerpt":"jdhaheoifnkf",
        "content":""" Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam, cum alias. Dicta officiis cupiditate laborum temporibus molestias. Doloribus earum dolore aspernatur doloremque eum aperiam neque debitis. Reiciendis, doloremque voluptatibus! Ducimus.
         
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam, cum alias. Dicta officiis cupiditate laborum temporibus molestias. Doloribus earum dolore aspernatur doloremque eum aperiam neque debitis. Reiciendis, doloremque voluptatibus! Ducimus.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam, cum alias. Dicta officiis cupiditate laborum temporibus molestias. Doloribus earum dolore aspernatur doloremque eum aperiam neque debitis. Reiciendis, doloremque voluptatibus! Ducimus.
        """
    }
]

def getdate(post):
    return post['date']

# def index(request):
#     # sorted_posts=sorted(allposts,key=getdate)
#     # latest_posts=sorted_posts[-3:]
#     latest_posts=Post.objects.all().order_by("-date")[0:3]
#     print(latest_posts)
#     return render(request,"blog/index.html",{"posts":latest_posts})

#class based method for index
class IndexView(ListView):
    template_name="blog/index.html"
    model=Post
    context_object_name="posts"
    def get_queryset(self):
        query_set=super().get_queryset()
        data=query_set.order_by("-date")[0:3]
        return data




# def posts(request):
#     allposts=Post.objects.all().order_by("-date")
#     return render(request,"blog/all-posts.html",{'all_posts': allposts})

#class based view for posts
class AllpostsView(ListView):
    template_name="blog/all-posts.html"
    model=Post
    context_object_name="all_posts"
    ordering=["-date"]


# def post_details(request,slug):
#     # selected=next(post for post in allposts if post['slug']==slug)
#     # print(selected)
#     # selected=Post.objects.get(slug=slug)
#     selected=get_object_or_404(Post,slug=slug)

#     return render(request,"blog/post-detail.html",
#                   {"posts":selected,
#                        "tags":selected.tags.all()                                     
#                                                    })

#class based view for post_details
# class PostdetailsView(DetailView):
#     template_name="blog/post-detail.html"
#     model=Post
#     context_object_name="posts"
#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         # context["tags"]=context["posts"].tags.all()
#         context["tags"]=self.object.tags.all()
#         context["comment_form"]=CommentForm()
#         return context
    
#basic View based method for the above    
class PostdetailsView(View):
    def get(self,request,slug):
        selected=Post.objects.get(slug=slug)
        selected=get_object_or_404(Post,slug=slug)
        stored_posts=request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later=selected.id in stored_posts
        else:
            is_saved_for_later=False    
        
        return render(request,"blog/post-detail.html",
                  {"posts":selected,
                    "tags":selected.tags.all(),
                    "comment_form" : CommentForm(), 
                    #one to many relation with related name 
                    "comments": selected.comments.all().order_by("-id"),
                    "is_saved_for_later":is_saved_for_later                                
                    })
    def post(self,request,slug):
        comment_form=CommentForm(request.POST)
        selected=get_object_or_404(Post,slug=slug)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.post=selected
            comment.save()
            redirect_url=reverse("post-details-page",kwargs={"slug":slug})
            return redirect(redirect_url) 
        selected=Post.objects.get(slug=slug)
        selected=get_object_or_404(Post,slug=slug)
        stored_posts=request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later=selected.id in stored_posts
        else:
            is_saved_for_later=False
        return render(request,"blog/post-detail.html",
                  {"posts":selected,
                    "tags":selected.tags.all(),
                    "comment_form" : comment_form,  
                    "comments": selected.comments.all().order_by("-id") ,
                    "is_saved_for_later":is_saved_for_later                                 
                    }) 


class ReadlaterView(View):
    def get(self,request):
        stored_posts=request.session.get("stored_posts")
        context={}
        if stored_posts is None or len(stored_posts)==0:
            context["posts"]=[]
            context["has_posts"]=False
        else:
            print(stored_posts)
            context["posts"]= Post.objects.filter(id__in=stored_posts) 
            context["has_posts"]=True   

           
        return render(request,"blog/stored-posts.html",context)



    def post(self,request):
        stored_posts=request.session.get("stored_posts")
        post_id=int(request.POST["post_id"])
        if stored_posts is None:
            stored_posts=[]
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)    
        request.session['stored_posts'] = stored_posts  
        return redirect("starting-page")        
           


