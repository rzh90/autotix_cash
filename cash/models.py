from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Show(models.Model):
    THEATRES = (
        ('Ambassador', 'Chicago'),
        ('Gershwin', 'Wicked'),
        ('Majestic', 'The Phantom of the Opera'),
        ('Schoenfeld', 'Come From Away'),
        ('Shubert', 'To Kill a Mockingbird'),
    )
    show = models.CharField(max_length=200, choices=THEATRES)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.get_show_display()


class Spent(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    amount = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'spent'

    def __str__(self):
        return f'${self.amount}'
