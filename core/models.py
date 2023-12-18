from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()



class product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    datecreated = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to="product")
    size = models.IntegerField(default=32)