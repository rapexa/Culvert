from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=512)

    def __str__(self):
        return "{} - {}".format(self.user, self.token)