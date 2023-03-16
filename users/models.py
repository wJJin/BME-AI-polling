from .choices import *

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, user_id, password, **extra_fields):
        user = self.model(
            user_id = user_id,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password):
        user = self.create_user(user_id, password,)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.level = 0
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    '''
    user_id는 학번
    '''
    
    objects = UserManager()
    user_id = models.CharField(max_length=15, verbose_name="아이디", unique=True)
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    level = models.CharField(choices=LEVEL_CHOICES, max_length=18, verbose_name="등급", default=2)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    
    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "USER_TB"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"


class PollingImage(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아이디')
    user_vote = models.CharField(choices=IMAGE_CHOICES, max_length=5, verbose_name="투표번호", null=True)
    name_vote = models.CharField(choices=NAME_CHOICES, max_length=255, verbose_name="이미지명", null=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        db_table = "PIMAGE_TB"
        verbose_name = "투표이미지"
        verbose_name_plural = "투표이미지"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)