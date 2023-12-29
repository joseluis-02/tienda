
from django.urls import path
# Views
from .views import LoginUserTemplateView
urlpatterns = [
    path(
        'login/', 
        LoginUserTemplateView.as_view(),
        name='login',
        ),
]