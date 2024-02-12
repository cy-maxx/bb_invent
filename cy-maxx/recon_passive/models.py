from django.db import models

# Create your models here.

class WhoisInformation(models.Model):
    domain_name = models.CharField(max_length=255, primary_key=True)
    registrar = models.CharField(max_length=255, blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    registrant_name = models.CharField(max_length=255, blank=True, null=True)
    registrant_email = models.EmailField(blank=True, null=True)
    nameservers = models.TextField(blank=True, null=True)
    raw_data = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.domain_name