from django.db import models
import uuid
# Create your models here.

class Book(models.Model):
    id = models.UUIDField('Book Id',primary_key=True, default = uuid.uuid4, help_text="generated unique id for book")
    name = models.CharField(max_length=100, help_text='Book Name',null=True)
    purchase_date = models.DateField(null=True, blank=True)
    genre = models.ManyToManyField('Genre', help_text='genre of book')
    author = models.ForeignKey('Author',on_delete=models.SET_NULL ,help_text='Book Author', null=True)
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Author(models.Model):
    author_name = models.CharField(max_length=100, help_text='Name of Author',null=True)
    numChoice = (
        ('1','One'),
        ('2','Two'),
        ('3','Three'),
        ('4','Four'),
        ('5', 'Five')
    )
    total_book_written = models.CharField(max_length=1, choices=numChoice)
    date_of_birth = models.DateField('Birth',null=True, blank=True)
    date_of_death = models.DateField('Death',null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.author_name

class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Book Name',null=True)
    choice=(
        ('1','One'),
        ('2','Two'),
        ('3','Three'),
        ('4','Four'),
        ('5', 'Five')
    )
    ratings=models.CharField(max_length=1,choices=choice)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 

class student(models.Model):
    sname = models.CharField(max_length=100, help_text='Book Name',null=True)
    Choice=(
        ('1','One'),
        ('2','Two'),
        ('3','Three'),
        ('4','Four'),
        ('5', 'Five')
    )
    books_purchased= models.CharField(max_length=1,choices=Choice)
    def __str__(self):
        return self.sname