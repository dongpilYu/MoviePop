from django.db import models


# Create your models here.
class Predict(models.Model):
    url = models.TextField()
    title = models.CharField(max_length=128)
    image_url = models.TextField()
    rating_before = models.FloatField()
    rating_after = models.FloatField()
    num_news = models.IntegerField(default=0)
    distributor = models.IntegerField(default=0)
    num_viewers = models.IntegerField(default=0)

    def __str__(self):
        return self.title
