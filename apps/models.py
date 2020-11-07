from django.db import models
from django.urls import reverse

# Create your models here.

class post(models.Model):
    Title = models.CharField(max_length = 150)
    Author = models.CharField(max_length = 15)
    Date = models.DateTimeField(auto_now_add=True)
    Article = models.TextField(max_length = 400)

    def __str__(self):
        return self.Title + '|' + str(self.Author)
    

    def get_absolute_url(self):
        return reverse("detail", args=(str(self.id)))
    
class message(models.Model):
    name = models.CharField(max_length=20)
    messagei = models.TextField()
    number = models.IntegerField()

    def __str__(self):
        return self.name
