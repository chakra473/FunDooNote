from django.db import models
from django.contrib.auth.models import User


class UserAuth(User):
    address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(
            f"username:{self.username}\nfirstname:{self.first_name}\nlastname:{self.last_name}\nemail:{self.email}"
            f"\naddress:{self.address}\nphone number:{self.phone_number}")

    # Create your models here.
