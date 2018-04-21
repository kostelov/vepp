from django.db import models
from django.contrib.auth.models import AbstractUser


class ProjectUser(AbstractUser):
    parent_name = models.CharField(verbose_name='по-батькові', max_length=20, blank=True)
    date_of_birth = models.DateField(verbose_name='дата народження', blank=True, null=True)
    phone1 = models.CharField(verbose_name='номер телефона', max_length=16, blank=True)
    phone2 = models.CharField(verbose_name='номер телефона', max_length=16, blank=True, null=True)
    avatar = models.ImageField(verbose_name='фото', upload_to='users_avatars', blank=True)
    is_dir = models.BooleanField(verbose_name='керівник', default=False)
    is_assistant = models.BooleanField(verbose_name='помічник', default=False)
    is_client = models.BooleanField(verbose_name='клієнт', default=False)

    def __str__(self):
        return self.username
