from django.urls import path
from rest_framework.routers import SimpleRouter
from materials.views import LessonCreateApiView, LessonListApiView, LessonRetrieveApiView, LessonUpdateApiView, \
    LessonDestroyApiView, SubscriptionCreateAPIView

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register(r'courses', CourseViewSet, basename='courses')
# router.register(r'subscription', SubscriptionViewSet, basename='subscription')


urlpatterns = [
    path('lesson/', LessonListApiView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveApiView.as_view(), name='lesson_retrieve'),
    path('lesson/create/', LessonCreateApiView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/delete/', LessonDestroyApiView.as_view(), name='lesson_delete'),
    path('lesson/<int:pk>/update/', LessonUpdateApiView.as_view(), name='lesson_update'),
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
]

urlpatterns += router.urls
