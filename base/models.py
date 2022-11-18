from django.db import models

# Create your models here.

class MangaTitle(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    chapterCount = models.PositiveSmallIntegerField(default=1)
    volumeCount = models.PositiveSmallIntegerField(default=0)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    firstCoverImage = models.ImageField(upload_to='base/uploads/covers', null=True, blank=True)

    authors = models.TextField(null=True, blank=True) #TODO: add relation with Author model
    status = models.CharField(max_length=200, null=True) #TODO: add enum
    genres = models.TextField(null=True, blank=True) #TODO: think what to do with it

    def __str__(self):
        return self.name
