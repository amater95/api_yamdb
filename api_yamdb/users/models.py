from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole:
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    choices = [
        (USER, 'user'),
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator'),
    ]


class User(AbstractUser):
    """Модель для работы с пользователями"""
    email = models.EmailField(
        verbose_name='email адрес',
        max_length=254,
        unique=True,
        blank=False
    )
    bio = models.TextField(blank=True,)
    role = models.CharField(
        max_length=15,
        choices=UserRole.choices,
        default=UserRole.USER
    )
    confirmation_code = models.CharField(
        max_length=255, blank=True, null=True
    )
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('username', 'email',),
                name='unique_fields'
            ),
        ]

    def __str__(self) -> str:
        return self.username

    @property
    def is_moderator(self):
        """True для пользователей с правами модератора."""
        return self.role == UserRole.MODERATOR

    @property
    def is_admin(self):
        """True для пользователей с правами админа и суперпользователей."""
        return (
            self.role == UserRole.ADMIN
            or self.is_staff
            or self.is_superuser
        )
