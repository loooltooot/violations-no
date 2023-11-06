from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

# Create your models here.

class MyUser(AbstractUser):
    patronymic = models.CharField(_('patronymic'), max_length=150)
    tel = models.CharField(_('phone number'), max_length=24, unique=True, help_text=_('Example: +7(XXX)-XXX-XX-XX'))   

    @admin.display(
        ordering='last_name',
        description=_('Full name')
    )
    def get_fio(self):
        full_name = []

        if self.last_name:
            full_name.append(self.last_name.strip())
        if self.first_name:
            full_name.append(self.first_name.strip())
        if self.patronymic:
            full_name.append(self.patronymic.strip())

        return ' '.join(full_name)
        
class Report(models.Model):
    class Meta:
        verbose_name = _('violation report')
        verbose_name_plural = _('violation reports')

    STATUS_CHOICES = [
        ('new', _('new')),
        ('accepted', _('accepted')),
        ('declined', _('declined')),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    report_description = models.TextField(_('violation description'), max_length=1500)
    car_plate = models.CharField(_('license plate number'), max_length=24)
    status = models.CharField(_('status'), max_length=10, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f'{self.user.get_fio()} | {self.car_plate}'
    