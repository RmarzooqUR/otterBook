from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    asset = models.FileField()
    votes = models.PositiveIntegerField(default=0)

class Comment(models.Model):
    comment = models.TextField(null=True)
    book = models.ForeignKey(Book, related_name='book',on_delete=models.CASCADE)
