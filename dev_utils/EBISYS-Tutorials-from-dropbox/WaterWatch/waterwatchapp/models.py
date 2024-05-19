#from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class WaterConsumption(models.Model):
    Id = models.IntegerField(primary_key=True)
    Suburb = models.CharField(max_length=100)
    NoOfSingleResProp = models.IntegerField()
    AvgMonthlyKL = models.IntegerField()
    AvgMonthlyKLPredicted = models.IntegerField()
    PredictionAccuracy = models.IntegerField()
    Month = models.CharField(max_length=50)
    Year = models.IntegerField()
    DateTime = models.DateTimeField()
    geom = models.PointField()

    def __str__(self):
        return self.Suburb

    class Meta:
        verbose_name_plural = 'WaterConsumption'
