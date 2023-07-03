from django.http import Http404
from django.shortcuts import render
from .models import Book
from django.db.models import Avg, Min, Max

# Create your views here.

def index(request):
    books=Book.objects.all()
    total_count=books.count
    avg_rating=books.aggregate(Avg("rating"))
    print("avg_rating",avg_rating)

    return render(request,"book_outlet/index.html", 
                  {"books":books,
                   "total_count":total_count,
                   "avg_rating":avg_rating
                   })

def book_details(request,slug):
    try:
        bookobj=Book.objects.get(slug=slug)
    except:
        raise Http404()    
    print(bookobj)
    context={
        'title':bookobj.title,
        "author":bookobj.author,
        "rating":bookobj.rating,
        "is_bestselling":bookobj.is_bestselling
    }
    
    return render(request,"book_outlet/bookdetail.html",context)

# def book_details(request,id):
#     try:
#         bookobj=Book.objects.get(id=id)
#     except:
#         raise Http404()    
#     print(bookobj)
#     context={
#         'title':bookobj.title,
#         "author":bookobj.author,
#         "rating":bookobj.rating,
#         "is_bestselling":bookobj.is_bestselling
#     }
    
#     return render(request,"book_outlet/bookdetail.html",context)


