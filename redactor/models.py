# -*- coding: utf-8 -*-
import Image
from django.conf import settings
from django.db import models
import datetime


MAX_SIZE = getattr(settings, 'REDACTOR_PHOTOS_AUTORESIZE', (640, 480))


class File(models.Model):
    upload = models.FileField(upload_to="upload/redactor/%Y/%m/%d/")
    date_created = models.DateTimeField(default=datetime.datetime.now)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super(File, self).save(*args, **kwargs)
        if self.is_image:
            img = Image.open(self.upload.path)
            if img.size > MAX_SIZE:
                img.thumbnail(MAX_SIZE, Image.ANTIALIAS)
                img.save(self.upload.path)
