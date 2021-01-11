from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.urls import reverse
from autoslug import AutoSlugField


class Show(models.Model):
    AMBASSADOR = 'Chicago'
    GERSHWIN = 'Wicked'
    MAJESTIC = 'The Phantom of the Opera'
    SCHOENFELD = 'Come From Away'
    SHUBERT = 'To Kill a Mockingbird'

    THEATRES = (
        (AMBASSADOR, 'Chicago'),
        (GERSHWIN, 'Wicked'),
        (MAJESTIC, 'The Phantom of the Opera'),
        (SCHOENFELD, 'Come From Away'),
        (SHUBERT, 'To Kill a Mockingbird'),
    )

    show = models.CharField(max_length=200, choices=THEATRES)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # slug = models.SlugField(null=False, unique=True)
    slug = AutoSlugField(populate_from='show')

    def __str__(self):
        return self.get_show_display()

    def get_absolute_url(self):
        return reverse('cash:shows', kwargs={'slug': self.slug})


class Spent(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    amount = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'spent'

    def __str__(self):
        return f'${self.amount}'
