from django.urls import path

from .views import AppView

app_name = 'service_app'
urlpatterns = [
    path('', AppView.as_view(), name='app'),
]
