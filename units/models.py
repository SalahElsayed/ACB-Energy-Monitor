from django.db import models


# ACB Unit 
class ACBUnit(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive')
    )
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def __str__(self):
        return self.name


# Unit Consumption 
class UnitConsumption(models.Model):
    unit = models.ForeignKey(ACBUnit, on_delete=models.CASCADE, related_name='consumption')
    energy_consumption = models.FloatField()
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.unit.name} - {self.energy_consumption} - {self.created_at}' 
