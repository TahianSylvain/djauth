from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=60, blank=True)
    pdp = models.ImageField(upload_to='profiling_photo', default='./logo_ispm.jpeg')
    sex = [
        ('M', 'Masculine'),
        ('F', 'feminine')
    ]
    gender = models.CharField(max_length=10, choices=sex)

    def __str__(self) -> str:
        return f'{self.user} - {self.id}'
