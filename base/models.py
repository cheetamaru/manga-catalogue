from django.db import models

# Create your models here.

class MangaTitle(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    firstCoverImage = models.TextField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    startDate = models.DateTimeField(null=True)
    endDate = models.DateTimeField(null=True)
    chapterCount = models.IntegerField(default=1)
    volumeCount = models.IntegerField(default=0)
    status = models.CharField(max_length=200, null=True)
    genres = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
