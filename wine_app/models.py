from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    grape_type = models.CharField(max_length=100)
    sugar = models.FloatField()
    brix = models.FloatField()
    ph = models.FloatField()
    acidity = models.FloatField()
    harvest_date = models.DateField()
    wine_style = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name
