from django.db import models
#Book {ISBN (PK), Title, AuthorID (FK), Publisher, PublishDate, Price}
#Author {AuthorID (PK), Name, Age, Country}
class Author(models.Model):
	AuthorID = models.CharField(max_length=30)
	Name=models.CharField(max_length=30)
	Age=models.IntegerField()
	Country=models.CharField(max_length=30)
class book(models.Model):
	ISBN = models.CharField(max_length=30)
	Title = models.CharField(max_length=30)
	AuthorID = models.CharField(max_length=30)
	Publisher = models.CharField(max_length=30)
	PublishDate = models.DateField()
	Price = models.IntegerField()
# Create your models here.
