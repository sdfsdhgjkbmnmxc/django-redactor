# -*- coding: utf-8 -*-
from django.db import models
import datetime


class File(models.Model):
    upload = models.FileField(upload_to="upload/redactor/%Y/%m/%d/")
    date_created = models.DateTimeField(default=datetime.datetime.now)
    is_image = models.BooleanField(default=True)
