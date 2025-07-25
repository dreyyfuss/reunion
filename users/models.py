from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        if not extra_fields.get("is_superuser"):
            extra_fields["is_active"] = False
            extra_fields["is_staff"] = False  # default for regular users

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Added back
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        """
        Returns the user's full name from their registration if it exists,
        otherwise returns None.
        """
        try:
            if hasattr(self, 'registration'):
                return f"{self.registration.first_name} {self.registration.last_name}"
            return None
        except Exception:
            return None

    @property
    def first_name(self):
        """
        Returns the user's first name from their registration if it exists,
        otherwise returns None.
        """
        try:
            if hasattr(self, 'registration'):
                return self.registration.first_name
            return None
        except Exception:
            return None

    @property
    def last_name(self):
        """
        Returns the user's last name from their registration if it exists,
        otherwise returns None.
        """
        try:
            if hasattr(self, 'registration'):
                return self.registration.last_name
            return None
        except Exception:
            return None