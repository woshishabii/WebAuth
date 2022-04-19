import uuid
from django.db import models


class Instance(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    version = models.CharField(max_length=50)
    force = models.BooleanField()
    views = models.IntegerField(default=0)
    link = models.CharField(max_length=200, blank=True)
    announcement = models.TextField(blank=True)
    update = models.TextField(blank=True)
    md5 = models.CharField(max_length=32, blank=True)

    class Meta:
        verbose_name = '实例'
        verbose_name_plural = '实例'

    def __str__(self):
        return self.name


class AuthCard(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    created = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField()
    mac = models.UUIDField(default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = '卡密'
        verbose_name_plural = '卡密'

    def __str__(self):
        return self.description
