from django.urls import path
from .views import hello  # 当前目录下的类，需要加“ . ”

urlpatterns = [
    path('hello/', hello, name='hello')
]