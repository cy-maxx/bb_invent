from django.db import models

# Create your models here.

class ProjectInfo(models.Model):
    app_name = models.CharField(max_length=100, primary_key=True)
    github_link = models.URLField()
    remark = models.TextField()

    def __str__(self):
        return self.app_name