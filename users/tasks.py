import datetime

from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils import timezone

from users.models import User


@shared_task
def check_user_activity():
    """ Проверка активности пользователя, если более 30 дней, то user.is_active = False"""

    user = get_user_model()
    deadline_data = timezone.now() - datetime.timedelta(days=30)
    # фильтр пользователей по дате -deadline_data, активный пользователь и нелогиневшемуся пользователю
    inactive_users = user.objects.filter(last_login__lt=deadline_data, is_active=True, last_login=not None)
    inactive_users.update(is_active=False)
    print(f'Deactivated {inactive_users.count()} users')