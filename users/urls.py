from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserListApiView, UserRetrieveApiView, UserDestroyApiView, UserUpdateApiView, UserCreateApiView, \
    PaymentListApiView
from materials.apps import MaterialsConfig
from materials.views import CourseViewSet

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register('', CourseViewSet)


urlpatterns = [
    path('register/', UserCreateApiView.as_view(), name='user_register'),
    path('', UserListApiView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserRetrieveApiView.as_view(), name='user_retrieve'),
    path('user/<int:pk>/delete', UserDestroyApiView.as_view(), name='user_delete'),
    path('user/<int:pk>/update', UserUpdateApiView.as_view(), name='user_update'),
    path('payments/', PaymentListApiView.as_view(), name='payments_list'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls