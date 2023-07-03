from django import forms
from . models import Review

# class ReviewForm(forms.Form):
#     user_name=forms.CharField(label="Enter username",
#                               required=True,
#                               max_length=10,
#                               min_length=3,
#                               error_messages={
#             "required": "This field is required",
#             "min_length": "Username must be at least 3 characters long",
#             "max_length": "Username can be at most 10 characters long",
#         }
#         )
#     review_text=forms.CharField(label="Your review",widget=forms.Textarea,max_length=200)
#     rating=forms.IntegerField(label="Your rating",min_value=1,max_value=5)
    


#this will define form fields automatically based on the model Review fields
#we specifies the related model name and the fields we taken or excluded
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields="__all__"
        # exclude=["owner_comment"]
        labels={
            "user_name":"Your name",
            "review_text":"Your review",
            "rating":"rating"
        }
        error_messages={
            "user_name":{
                "required":"username must not be empty",
                "min_length": "Username must be at least 3 characters long",
            }
        }