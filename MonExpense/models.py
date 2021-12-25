from django.db import models


class Transaction(models.Model):
    card_user = models.CharField(max_length=50, blank=True, null=True)
    card = models.CharField(max_length=10, blank=True, null=True)
    trans_date = models.DateField(auto_now=False, auto_now_add=False)
    trans_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    trans_location = models.CharField(max_length=10, blank=True, null=True)
    pass
