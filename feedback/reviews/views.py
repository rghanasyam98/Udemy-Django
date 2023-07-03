from typing import Any
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView


from reviews.models import Review
from . forms import ReviewForm

# Create your views here.

#class based view
# class ReviewView(View):
#     #all get requests automatically enters into this no need of if checking
#     def get(self,request):
#         form=ReviewForm()
#         return render(request,"reviews/reviews.html", {"form":form})
         
#     #all post requests automatically enters into this no need of if checking

#     def post(self,request):
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()

#             return redirect("thankyou")
#         else:
#             form=ReviewForm()
#             return render(request,"reviews/reviews.html",{"form":form})

        

#example with FormView
# class ReviewView(FormView):
#     form_class=ReviewForm #for identifying which form class
#     template_name="reviews/reviews.html"
#     success_url="thankyou/"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
    


#example with CreateView more specific method for handling form 
class ReviewView(CreateView):
    model=Review #name of the table date to be saved
    form_class=ReviewForm #for identifying which form class to passs to template
    template_name="reviews/reviews.html" #pass to which template
    success_url="thankyou/" #redirecting path after successfull form submission

       




# def review(request):
#     # iserror=False
#     # if request.method == "POST":
#     #     uname=request.POST['username']
#     #     # print(uname)
#     #     if uname == "":
#     #         iserror=True
#     #         return render(request,"reviews/reviews.html",{
#     #     "iserror":iserror
#     # })
#     #     return redirect("thankyou")
    
#     # return render(request,"reviews/reviews.html",{
#     #     "iserror":iserror
#     # })
#     if request.method == "POST":
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['user_name'])
#             #if using regular form
#             # review=Review(
#             #     user_name=form.cleaned_data['user_name'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating']
#             # )
#             # review.save()


#             #if using model form
#             form.save()

#             return redirect("thankyou")
#     else:
#         form=ReviewForm()


#     return render(request,"reviews/reviews.html",
#                   {
#                        "form":form
#                    }
#                   )
         



#function based view
# def thankyou(request):
#      return render(request,"reviews/thankyou.html")
           

#class based view by extending View
# class ThankyouView(View):
#     def get(self,request):
#         return render(request,"reviews/thankyou.html")



#class based view by extending TemplateView
#the get() and post() will not work here they are not belongs to TemplateView but in View
class ThankyouView(TemplateView):
    template_name="reviews/thankyou.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["message"]="This works!"
        return context



# class ReviewListView(TemplateView):
#     template_name="reviews/reviewlist.html"
#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         reviews=Review.objects.all()
#         context["reviews"]=reviews
#         return context

#more specific view for list of items rendering
class ReviewListView(ListView):
    template_name="reviews/reviewlist.html"
    model=Review #list of data taken from which model
    context_object_name="reviews" #name of the key that we uses in the template

    #if we dont want to display all the data but only based on some filter condition
    # def get_queryset(self):
    #     base_query= super().get_queryset()
    #     filter_data=base_query.filter(rating__gte=4)
    #     return filter_data
    
    
# class ReviewDetailView(TemplateView):
#      template_name="reviews/reviewdetails.html"
#      def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         review_id=kwargs["id"]
#         review=Review.objects.get(pk=review_id)
#         context["review"]=review
#         return context
       

#data will be automatically matched with passed id
class ReviewDetailView(DetailView):
    template_name="reviews/reviewdetails.html"
    model=Review  #by default it takes "review" as key for template
    #to add more data to the context data
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)#this is already added data
        #this method will results an error if fav_review_id is not set in session already
        # fav_review_id=self.request.session["fav_review_id"]
        #alternate method
        fav_review_id=self.request.session.get("fav_review_id")
        if fav_review_id == str(self.object.id):
            context["is_favorite"]=True
        else:
            context["is_favorite"]=False
        return context    

    


    #example for UpdateView and DeleteView
#     from django.views.generic import UpdateView, DeleteView
# from django.urls import reverse_lazy

# class ReviewUpdateView(UpdateView):
#     model = Review
#     form_class = ReviewForm
#     template_name = 'reviews/review_update.html'
#     success_url = reverse_lazy('reviewlist')

# class ReviewDeleteView(DeleteView):
#     model = Review
#     template_name = 'reviews/review_confirm_delete.html'
#     success_url = reverse_lazy('reviewlist')

class AddFavoriteView(View):
    def post(self,request):
        fav_review_id=request.POST['review_id']
        # fav_review=Review.objects.get(pk=fav_review_id)
        request.session["fav_review_id"]=fav_review_id
        redirect_url=reverse("reviewdetails",kwargs={"pk":fav_review_id})
        return redirect(redirect_url)
