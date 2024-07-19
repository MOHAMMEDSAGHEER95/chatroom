from django.db import models


class User(models.Model):
    username = models.CharField(max_length=266)

    class Meta:
        verbose_name = "chatuser"
        verbose_name_plural = "chatusers"

    def __str__(self):
        return self.username