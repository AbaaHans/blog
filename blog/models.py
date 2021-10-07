from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_ate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title