from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название',
        help_text='Укажите название курса'
    )
    image = models.ImageField(
        upload_to='users/avatars',
        verbose_name='Превью ',
        help_text='Укажите Превью'
    )
    description = models.TextField(
        verbose_name='Название',
        help_text='Укажите название курса',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название',
        help_text='Укажите название курса',
        ** NULLABLE
    )
    image = models.ImageField(
        upload_to='users/avatars',
        verbose_name='Превью ',
        help_text='Укажите Превью'
    )
    description = models.TextField(
        verbose_name='Название',
        help_text='Укажите название курса',
        **NULLABLE
    )
    video = models.CharField(
        max_length=250,
        verbose_name='Ссылка на видео',
        help_text='Укажите ссылку на видео',
        **NULLABLE
    )
    course = models.ForeignKey(
        to=Course,
        on_delete=models.SET_NULL,
        verbose_name='Курс',
        help_text='Укажите курс',
        **NULLABLE
    )


    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
