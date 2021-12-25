from django.db import models


class UserProfile(models.Model):
    BANK = [
        ('BMO', 'BMO'),
        ('RBC', 'RBC'),
        ('CIBC', 'CIBC'),
        ('TD', 'TD'),
        ('SCOTIA BANK', 'SCOTIA BANK'),
    ]
    user = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default='no email')
    bank = models.CharField(choices=BANK, max_length=50)
    card = models.CharField(max_length=50)
    card_note = models.CharField(max_length=550)
