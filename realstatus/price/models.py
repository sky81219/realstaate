from typing import Dict, List
from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin


class TimeStempedInitalization(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract: bool = True
        ordering: List[str] = ["-created_at", "-updated_at"]
        

class StockInformation(TimeStempedInitalization):
    pass

    class Meta:
        db_table: str = "stock_status"


class RealStatusInformation(TimeStempedInitalization):
    pass

    class Meta:
        db_table: str = "real_status"


class CustomUserManager(BaseUserManager):    
    def create_user(self, name: str, email: str, password: str, **extra_fields):
        """
        유저정보는 최대한 간단하게 
        """
        if not email:
            raise ValueError("이메일 or 이름을 확인해주세요..!")
        elif not name:
            raise ValueError("이메일 or 이름을 확인해주세요..!")
        
        email: str = self.normalize_email(email)
        user = self.model(name=name, email=email, password=password, **extra_fields)
        user.password = make_password(password=password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email: str, name: str = None, password: str = None, **extra_fields):
        if password is None:
            raise ValueError("패스워드를 입력하셧는지 확인해주세요..!")
        
        user = self.create_user(
            email=self.normalize_email(email), 
            name=name,
            password=password
        )
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
    
    
class BasicUserInformation(AbstractBaseUser, PermissionsMixin, TimeStempedInitalization):
    email = models.EmailField(max_length=50, unique=True, null=False, blank=True, verbose_name="email")
    name = models.CharField(max_length=10, primary_key=True, blank=False, null=False, verbose_name="name")
    is_active = models.BooleanField(default=True, verbose_name="active")
    is_superuser = models.BooleanField(default=False)

    # Manager setting
    objects = CustomUserManager()
    
    @property
    def is_staff(self):
        return self.is_superuser
    
    # field 설정 
    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: List[str] = ["name"]
        
    class Meta:
        db_table: str = "basic_user"
    

