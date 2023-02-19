from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('225d2cad-9f26-44dd-abdf-831d2d275327', views.whatsAppWebhook, name='whatsapp'),
]