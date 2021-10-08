from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    """Model to define the fields required  displayed in
   """
    title = models.CharField(max_length=200)
    comments = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
