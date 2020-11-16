from django.urls import path
from users.api.views import UserDisplayAPIView

urlpatterns = [
    path("user/", UserDisplayAPIView(), name="current-user")
]