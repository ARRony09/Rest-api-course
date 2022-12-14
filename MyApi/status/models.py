from django.db import models
from django.conf import settings
# Create your models here.


class StatusModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)[0:30]

    class Meta:
        verbose_name_plural = "Status List"
