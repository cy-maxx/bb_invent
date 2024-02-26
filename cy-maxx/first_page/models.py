from django.db import models

class Domain(models.Model):
    domain = models.CharField(primary_key=True, max_length=255)
    site = models.URLField()
    bugbounty = models.URLField()

    def __str__(self):
        return self.domain
