from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(max_length=500)


class ItemModel(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryModel)
    description = models.TextField(max_length=500)
    image = models.URLField(max_length=100, default="https:\\")

