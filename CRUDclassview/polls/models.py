from django.db import models

# Create your models here.
#from django.db import models

# Create your models here.

class Currencies(models.Model):
    iso = models.IntegerField()
    description = models.CharField(max_length=10)
    
    def __str__(self):
        return "%s %s" % (self.description, self.iso)