from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
import re


def validate_email(email_string):
    possible_match = re.match(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}', email_string)
    if possible_match is None:
        raise ValidationError(u'%s is not a valid email address' % email_string)


class Transaction(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, validators=[validate_email])
    service_description = models.CharField(max_length=500, default='placeholder')
    price = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    date_submitted = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name