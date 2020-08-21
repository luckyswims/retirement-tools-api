from django.db import models

# Create your models here.
class Annuity(models.Model):
    """Defines fields and methods of the Annuity resource model"""
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    duration = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        """Returns a string depiction of the model"""
        return f"An annuity (ID #{self.pk}) of ${self.amount} per month for {self.duration} months."

    def as_dict(self):
        """Returns dictionary version of the model"""
        return {
            'id': self.id,
            'amount': self.amount,
            'duration': self.duration
        }
