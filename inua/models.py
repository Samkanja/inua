from django.db import models
class Program(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300,unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/programs-pics/')

    def __str__(self) -> str:
        return self.title

class Activity(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300,unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/activity-pics/')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class AboutUs(models.Model):
    description = models.TextField()
    vision = models.CharField(max_length=255)
    mission = models.CharField(max_length=400)

