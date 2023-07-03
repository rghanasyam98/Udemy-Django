from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=30)
    code=models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name}, {self.code}"
    
    #to change the description on admin panel
    class Meta:
        verbose_name_plural="Countries"


class Address(models.Model):
    street=models.CharField(max_length=50)
    postal_code=models.CharField(max_length=5)
    city=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    #to change the description on admin panel
    class Meta:
        verbose_name_plural="Address entries"


class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.OneToOneField(Address, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    # author=models.CharField(max_length=100,null=True)
    author=models.ForeignKey(Author, on_delete=models.CASCADE,null=True,related_name="books")
    is_bestselling=models.BooleanField(default=False)
    slug=models.SlugField(default="", blank=True, 
                        #   editable=False,
                          db_index=True, null=False)
    #this field will be added as a list
    published_countries=models.ManyToManyField(Country)

    # def save(self,*args,**kwargs):
    #     self.slug=slugify(self.title)
    #     super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("book_details",args=[self.slug])   
    
    #  def get_absolute_url(self):
    #     return reverse("book_details",args=[self.id])

    def __str__(self):
        return f"{self.title} ({self.rating})"
    