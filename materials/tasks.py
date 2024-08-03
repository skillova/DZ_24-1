from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from materials.models import Subscription


@shared_task
def send_email_task(course_id):
    """ Send email to user """
    subs = Subscription.objects.filter(course=course_id)
    for sub in subs:
        course = sub.course
        user = sub.user
        send_mail('Обновление', 'Изменение на курсе'.format(course.name),
                  EMAIL_HOST_USER, [user.email])
        print(f'Send message {user.email} complete')
