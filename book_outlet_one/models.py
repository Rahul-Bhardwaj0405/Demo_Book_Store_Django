from typing import Any
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from traitlets import default
from django.urls import reverse
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    nationality = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)

    def author_info(self,*args):
        return f"{self.name}, {self.address}, {self.nationality}, {self.email}"
    
    def __str__(self):
        return self.author_info()
    
    
    class Meta:
        verbose_name_plural = "Author"


    

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    published_countries = models.CharField(max_length=100)

    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
     
    class Meta:
        verbose_name_plural = "Book"
    

    def book_info(self):
        return f"{self.title}, {self.rating}, {self.author}, {self.is_bestselling}, {self.slug}, {self.published_countries}"
    
    def __str__(self):
        return self.book_info()
