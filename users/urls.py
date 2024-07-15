from django.urls import path
from rest_framework.routers import SimpleRouter
from users.views import UserListApiView, UserRetrieveApiView, UserDestroyApiView, UserUpdateApiView, UserCreateApiView, \
    PaymentListApiView
from materials.apps import MaterialsConfig
from materials.views import CourseViewSet

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register('', CourseViewSet)


urlpatterns = [
    path('user/create', UserCreateApiView.as_view(), name='user_create'),
    path('', UserListApiView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserRetrieveApiView.as_view(), name='user_retrieve'),
    path('user/<int:pk>/delete', UserDestroyApiView.as_view(), name='user_delete'),
    path('user/<int:pk>/update', UserUpdateApiView.as_view(), name='user_update'),
    path('payments/', PaymentListApiView.as_view(), name='payments_list'),
]

urlpatterns += router.urls