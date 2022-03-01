from operator import mod
from django.db import models

from django.utils import timezone

from django.conf import settings
from django.urls import reverse
# Create your models here.

POST_STATUS = (
    ("draft", "Draft"),
    ("published", "Published"),
)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=9, choices=POST_STATUS)
    create_time = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name="post site"
        verbose_name_plural="post sites"

    def get_absolute_url(self):
        kwargs={
            "pk": self.pk
        }    
        return reverse("post-details", kwargs=kwargs)


    def __str__(self) -> str:
        return f"{self.title}"