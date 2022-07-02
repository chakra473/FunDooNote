from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=400)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.CharField(max_length=300, unique=True)

    # def __str__(self):
    #     return str(
    #         f"username:{self.user_name}\nfirstname:{self.first_name}\nlastname:{self.last_name}\nemail:{self.email}")
# Create your models here.
