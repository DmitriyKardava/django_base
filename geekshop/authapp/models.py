from datetime import timedelta
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


# Create your models here.

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(
        verbose_name='возраст', blank=True, null=True)
    activatio_key = models.UUIDField(default=uuid.uuid4)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))
    is_active = models.BooleanField(verbose_name='активный', default=False)
    
    def is_activatio_key_expired(self):
        return now() > self.activation_key_expires