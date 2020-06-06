from django.db import models


class Product(models.Model):
    productId = models.CharField(max_length=255, null=False)

    class Meta:
        app_label = "userReview"


class User(models.Model):
    userId = models.CharField(max_length=255, null=False)
    profileName = models.CharField(max_length=255, null=False)
    productId = models.ManyToManyField(to=Product, through='Review')

    class Meta:
        app_label = "userReview"


class Review(models.Model):
    userId = models.ForeignKey(to=User, on_delete=models.CASCADE)
    productId = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    helpfulness = models.CharField(max_length=255)
    score = models.FloatField(max_length=10)
    time = models.CharField(max_length=255, null=False)
    summary = models.TextField(null=False)
    text = models.TextField(null=False)

    class Meta:
        app_label = "userReview"




