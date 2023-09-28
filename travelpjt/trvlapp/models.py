from django.db import models

# Create your models here.
class places(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to="pics")
    desc=models.TextField()

    def __str__(self):
        return self.name


class TeamMembers(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to="pics")
    postn=models.TextField()