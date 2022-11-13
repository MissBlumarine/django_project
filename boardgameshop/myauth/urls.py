from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import MeView, LoginView, LogoutView, UserCreationView

app_name = "myauth"

urlpatterns = [
                  path("me/", MeView.as_view(), name="me"),
                  path("login/", LoginView.as_view(), name="login"),
                  path("logout/", LogoutView.as_view(), name="logout"),
                  path("register/", UserCreationView.as_view(), name="register"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
