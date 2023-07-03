from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
# def index(request):
#     return HttpResponse("This works")

def february(request):
    return HttpResponse("february")

context={
    "january":"january",
    "february":"february",
    "march":"march",
    "april":"april",
    "may":"may",
    "june":"june",
    "july":"july",
    "august":"august",
    "september":"september",
    "october":"october",
    "november":"november",
    "december":None
}

def index(request):
    list_items=""
    months=list(context.keys())
    for month in months:
        redirect_url=reverse("monthly_challenge_bymonth",args=[month])

        capitalized_month=month.capitalize()
        list_items+=f"<li><a href=\"{redirect_url}\">{capitalized_month}</a></li>"
    response_data=f"<ul>{list_items}</ul>"
    
    # return HttpResponse(response_data)
    context1={"months":list(context.keys())}
    return render(request,"challenges/index.html",context1)

def monthly_challenge_bymonth(request,month):
    months=list(context.keys())
    
    if month>len(months):
        return HttpResponseNotFound("Month not spoorted")
    redirect_month=months[month-1]
    redirect_url=reverse("monthly_challenge_bymonth",args=[redirect_month])
    # return HttpResponseRedirect("/challenges/"+redirect_month)
    return HttpResponseRedirect(redirect_url)


    
    
def monthly_challenge(request,month):
    text=None
    

    try:
        text=context[month]
    except:
        # response_page=render_to_string("404.html")
        # return HttpResponseNotFound(response_page)
        raise Http404()
    
    #convert html template to string nd pass in httpresponse

    # response_data=f"<h1>{text}</h1>"
    # response_data=render_to_string("challenges/challenge.html")
    # return HttpResponse(response_data)
    context1={'month':text,'month_name':month}
    return render(request,"challenges/challenge.html",context1)
