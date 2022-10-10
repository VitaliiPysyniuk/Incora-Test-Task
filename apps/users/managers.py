from django.contrib.auth.base_user import BaseUserManager

from .utils import normalize_phone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, phone, **extra_kwargs):
        email = self.normalize_email(email)
        phone = normalize_phone(phone)
        user = self.model(email=email, phone=phone, **extra_kwargs)
        user.set_password(password)
        user.save()
        return user
