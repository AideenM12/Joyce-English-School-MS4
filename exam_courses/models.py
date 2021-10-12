from django.db import models

# Create your models here.


class ExamCourse(models.Model):
    """
    A Model for Exam Courses
    """
    name = models.CharField(max_length=254)
    required_level = models.CharField(max_length=254)
    certification_awarded = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    start_date = models.CharField(default="01-01-2021", max_length=50)
    end_date = models.CharField(default="31-12-2021", max_length=50)
    hours = models.CharField(default="50", max_length=50)

    def __str__(self):
        return self.name
