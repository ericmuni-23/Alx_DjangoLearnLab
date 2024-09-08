
from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
    def create_user(self, username, email, password, date_of_birth, profile_photo):
        if not username:
            raise ValueError('Username is required')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            profile_photo=profile_photo
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, date_of_birth, profile_photo):
        user = self.create_user(
            username,
            email,
            password,
            date_of_birth,
            profile_photo
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    