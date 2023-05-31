from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Product(models.Model):
    class ChoiceColor(models.TextChoices):
        QORA = 'Qora'
        OQ = 'Oq'
        QIZIL = 'Qizil'
        KOK = "ko'k"
        YAHSIL = 'Yashil'

    title = models.CharField(max_length=155)
    image1 = models.ImageField(upload_to='product/', null=True, blank=True)
    image2 = models.ImageField(upload_to='product/', null=True, blank=True)
    image3 = models.ImageField(upload_to='product/', null=True, blank=True)
    color = models.CharField(max_length=25, choices=ChoiceColor.choices, default=ChoiceColor.OQ)
    price = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    aksiya = models.IntegerField()
    category = models.ForeignKey('app.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('categories', args=[str(self.pk)])

