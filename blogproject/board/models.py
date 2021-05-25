from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Blog(TimeStampModel):
    title = models.CharField(max_length=100)
    body = models.TextField()

    # 추가
    def __str__(self):
        return self.title