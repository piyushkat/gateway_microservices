from django.urls import path
from . import views
urlpatterns = [
    path('<str:service_name>/<str:endpoint>', views.api_handler, name='api_handler'),
]