from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Author(AbstractBaseUser):
    
    email = models.EmailField()
    last_name = models.CharField(max_length = 100)
    first_name = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 500)
