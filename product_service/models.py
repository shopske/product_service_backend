from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Product(models.Model):
    """Product details."""
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photoUrls = models.JSONField()
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.name
