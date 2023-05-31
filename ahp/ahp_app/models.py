from django.db import models

# Create your models here.
# to add models to migrations we run the command : python manage.py makemigrations
# python manage.py migrate
class user(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
