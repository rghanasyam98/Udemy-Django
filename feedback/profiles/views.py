from django.shortcuts import redirect, render
from django.views import View
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView

# Create your views here.

#for storing in folder that code is written in store_file()
def store_file(file):
    with open("temp/image.png","wb+") as img_file:
        for chunk in file.chunks():
            img_file.write(chunk)

class ProfileListView(ListView):
    model=UserProfile
    template_name="profiles/profileslist.html"
    context_object_name="profiles"

#in this case no form class is required django will automatically creates a form based on the fields in the specified model
#and also handles the form submission automatically
class CreateProfileView(CreateView):
    model=UserProfile
    template_name="profiles/create_profile.html"
    fields="__all__"
    success_url="/profiles"  
              
          
#basic view based method simple method is given above
# class CreateProfileView(View):
#     def get(self, request):
#         form=ProfileForm()
#         return render(request, "profiles/create_profile.html",{"form":form})

#     def post(self, request):
#         submitted_form=ProfileForm(request.POST,request.FILES)
#         if submitted_form.is_valid():
#             user_profile=UserProfile(image=request.FILES['user_image'])
#             user_profile.save()

#             print(submitted_form.cleaned_data['user_image'])
#             return redirect("profiles")
#         return render(request, "profiles/create_profile.html",{"form":submitted_form})


        # print(request.FILES["user_image"])
        #for storing in folder that code is written in store_file()
        # store_file(request.FILES["user_image"])
        
