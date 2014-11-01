from django.db import models

# Create your models here.
class Incident(models.Model):
    longitude = models.DecimalField(max_digits=4, decimal_places=3)
    latitude = models.DecimalField(max_digits=4, decimal_places=3)
    date = models.DateField(blank=True)
    description = models.TextField()
    address = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return "Longitude: " + self.longitude + ", Latitude: " + self.latitude