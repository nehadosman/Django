from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Category(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])

    def __str__(self):
        return self.name
    
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50, validators=[MinLengthValidator(10)])
    desc = models.TextField()
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    views = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class ISBN(models.Model):
    author_title = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=13, unique=True)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    

    

