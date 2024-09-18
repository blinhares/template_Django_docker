from django.urls import path
from . import views, apps

app_name = 'app_exemplo'

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes/<int:question_id>/', views.detail, name='detail'),
    path('form/', views.form, name='form'),
]