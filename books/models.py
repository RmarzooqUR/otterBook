from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(null=True, max_length=255)
    asset = models.FileField(upload_to='media/', null=True)
    votes = models.PositiveIntegerField(default=0)

class Comment(models.Model):
    comment = models.TextField(null=True)
    book = models.ForeignKey(Book, related_name='book',on_delete=models.CASCADE)
