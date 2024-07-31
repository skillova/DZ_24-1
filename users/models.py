from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {"null": True, "blank": True}

PAYMENT_METHOD = {
    'cash': 'наличные',
    'transfer': 'перевод'
}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="Почта",
        help_text="Укажите почту"
    )
    phone_number = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        help_text="Укажите номер телефона",
        **NULLABLE
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Страна",
        help_text="Укажите страну",
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Укажите аватар",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payment(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    date_of_payment = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата оплаты'
    )
    paid_course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        verbose_name='Курс',
        **NULLABLE
    )
    paid_lesson = models.ForeignKey(
        to=Lesson,
        on_delete=models.CASCADE,
        verbose_name='Урок',
        **NULLABLE
    )
    payment_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Сумма оплаты'
    )
    payment_method = models.CharField(
        max_length=20,
        default='transfer',
        choices=PAYMENT_METHOD,
        verbose_name='Способ оплаты'
    )
    session_id = models.CharField(
        max_length=255,
        verbose_name='ID сессии',
        **NULLABLE
    )
    link = models.CharField(
        max_length=400,
        verbose_name='Ссылка на оплату',
        **NULLABLE
    )

    def __str__(self):
        return f'Оплата для {self.user}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ['-date_of_payment']
