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

    audience_num = models.IntegerField(default=0)
    """
    # 11-11
    title = models.CharField(max_length=128)
    image_url = models.TextField()
    rating_before = models.FloatField()
    rating_after = models.FloatField()
    
    movie_code = models.IntegerField(default=0)
    naver_url = models.TextField() 
    # show & input & (rating - 2)

    screen_num_7 = models.IntegerField(default=0)
    show_num_7 = models.IntegerField(default=0)
    audience_num_7 = models.IntegerField(default=0)
    money_num_7 = models.IntegerField(default=0)
    # 7 days - 4

    distributor_effect = models.IntegerField(default=0)
    actor_effect = models.IntegerField(default=0)
    director_effect = models.IntegerField(default=0)
    # effect - 3
    
    age = models.IntegerField(default=0)
    nationality = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    # others - 3
        
    audience_num = models.IntegerField(default=0)
    """

    def __str__(self):
        return self.title
