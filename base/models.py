from django.db import models
from django.utils.translation import gettext_lazy as _

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

    class Status(models.TextChoices):
        FINISHED = 'finished', _('Finished')
        ONGOING = 'ongoing', _('Publishing')
        HIATUS = 'hiatus', _('On Hiatus')
        CANCELED = 'canceled', _('Discontinued')
        NOT_STARTED = 'notstarted', _('Not Yet Published')

    status = models.CharField(max_length=12, null=True, choices=Status.choices)

    authors = models.TextField(null=True, blank=True) #TODO: add relation with Author model
    genres = models.TextField(null=True, blank=True) #TODO: think what to do with it

    def __str__(self):
        return self.name
