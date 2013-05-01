import datetime
from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Place(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    description = models.CharField(max_length=200)
    lat = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    lon = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    def __unicode__(self):
        return self.name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
class Information(models.Model):
    place = models.ForeignKey(Place)