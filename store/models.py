from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name =  models.CharField(max_length= 100)

    def fullname(self):
      return f"{self.first_name} {self.last_name}"
    
    def __str__(self) :
      return self.fullname()

class book(models.Model) :

    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators = [MinValueValidator(0) , MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete= models.CASCADE, related_name="books", null=True) 
    # cascade means if author will delete then all book related to tht will also deleted
    is_bestSeller = models.BooleanField(default = False)
    slug = models.SlugField(default ="", null = False,db_index=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
     return reverse("book_detail", args=[self.slug])



