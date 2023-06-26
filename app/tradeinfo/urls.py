from django.urls import path

from . import views

app_name = 'tradeinfo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tradeinfo_id>/', views.detail, name='detail'),
]
