from django.db import models

# Create your models here.
class LongUrl(models.Model):
    
    # Id is to be generated externally when
    # the service scales at distribution.
    # This field is now created but not used.
    uid = models.IntegerField(default=0)

    url = models.CharField(max_length=512)
    
    def __str__(self):
        return "{},{}".format(self.id, self.url)
