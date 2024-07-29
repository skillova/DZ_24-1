from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class TestLessons(APITestCase):
    """ Тестирование уроков """

    def setUp(self) -> None:
        self.user = User.objects.create(email="example@example.com")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            name="Test",
            description="Основы Test"
        )
        self.lesson = Lesson.objects.create(
            course=self.course,
            name="Test Lesson",
            description="Test",
            owner=self.user,
            video="https://www.youtube.com/watch",
        )

    def test_create_lesson(self):
        """ Тестирование создания урока """

        url = reverse("materials:lesson_create")
        data = {
            "name": "Test Lesson",
            "description": "Test",
            "course": self.lesson.course.id,
            "video": "https://www.youtube.com/watch",
        }

        response = self.client.post(url, data=data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)
        self.assertEqual(data.get("name"), "Test Lesson")
        self.assertEqual(data.get("course"), self.lesson.course.id)
        self.assertEqual(data.get("video"), "https://www.youtube.com/watch")
        self.assertEqual(data.get("description"), "Test")

    def test_edit_lesson(self):
        """ Тестирование изменения урока """

        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {
            "name": "Test Lesson",
            "description": "Test1",
            "course": self.lesson.course.id,
            "video": "https://www.youtube.com/watch1",
        }

        response = self.client.put(url, data=data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)
        self.assertEqual(data.get("description"), "Test1")
        self.assertEqual(data.get("video"), "https://www.youtube.com/watch1")
        self.assertEqual(data.get("course"), self.lesson.course.id)
        self.assertEqual(data.get("owner"), self.lesson.owner.id)

    def test_read_lesson(self):
        """ Тестирование списка урока """

        url = reverse("materials:lesson_list")

        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("count"), 1)

    def test_retrieve_lesson(self):
        """ Тестирование просмотра одного урока """

        url = reverse("materials:lesson_retrieve", args=(self.lesson.pk,))

        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)
        self.assertEqual(data.get("description"), "Test")
        self.assertEqual(data.get("video"), "https://www.youtube.com/watch")
        self.assertEqual(data.get("course"), self.lesson.course.id)
        self.assertEqual(data.get("owner"), self.lesson.owner.id)

    def test_delete_lesson(self):
        """ Тестирование удаления урока """

        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='example@example.com')
        self.course = Course.objects.create(name='Програмное обеспечение')
        self.client.force_authenticate(user=self.user)
        self.url = reverse('materials:subscription_create')

    def test_subscription_activate(self):
        """Тест подписки на курс"""
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        response = self.client.post(self.url, data=data)
        data_res = response.json()
        print(data_res)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),{"message": "Подписка добавлена"},)
        self.assertTrue(Subscription.objects.all().exists(),)

    def test_sub_deactivate(self):
        """Тест отписки с курса"""
        Subscription.objects.create(user=self.user, course=self.course)
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        response = self.client.post(self.url, data=data)
        data_res = response.json()
        print(data_res)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            response.json(),
            {
                "message": "Подписка удалена",
            },
        )
        self.assertFalse(
            Subscription.objects.all().exists(),
        )
