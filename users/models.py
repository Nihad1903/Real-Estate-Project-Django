from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
import hashlib
import secrets
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    phone_number = PhoneNumberField(region='AZ', null=True, blank=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    verification_code_hash = models.CharField(max_length=128, blank=True, null=True)
    code_expiry = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone']

    objects = UserManager()

    def generate_verification_code(self):
        code = secrets.randbelow(900000) + 100000  
        self.verification_code_hash = hashlib.sha256(str(code).encode()).hexdigest()
        self.code_expiry = timezone.now() + timezone.timedelta(minutes=10)
        self.save()
        return code
    
    def verify_code(self, code):
        if not self.code_expiry or timezone.now() > self.code_expiry:
            return False
        return self.verification_code_hash == hashlib.sha256(str(code).encode()).hexdigest()
    
    def __str__(self):
        return self.email

