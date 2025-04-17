from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """自定义用户模型，继承Django内置的AbstractUser"""
    
    # 添加额外的字段
    bio = models.TextField('个人简介', blank=True)
    avatar = models.ImageField('头像', upload_to='user_avatars/', blank=True, null=True)
    position = models.CharField('职位', max_length=100, blank=True)
    organization = models.CharField('组织/单位', max_length=100, blank=True)
    
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
    
    def __str__(self):
        return self.username