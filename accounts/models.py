from django.db import models
from django.contrib.auth.models import User


class CRMProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='crm_profile')
    corporate_email = models.EmailField("Корпоративна пошта")
    crm_password = models.CharField("Пароль для CRM поля", max_length=255)

    def __str__(self):
        return self.user.username