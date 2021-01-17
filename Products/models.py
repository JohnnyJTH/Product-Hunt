import Products
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    body = models.TextField()

    url = models.TextField()
    votes = models.IntegerField(default=1)
    pub_date = models.DateTimeField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def date(self):
        return self.pub_date.strftime('%B %e, %Y')
