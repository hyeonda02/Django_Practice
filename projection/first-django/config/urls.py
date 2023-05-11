"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demos.views import calculator, lotto,lotto_result,lotto_index #demos폴더 안의 view.py의 파일 속에서 calculator 함수 가져옴 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/',calculator, name ='calculator'), #calculator/경로로 들어오면 calculator 함수를 실행해라 라는 의미이다.
    path('lotto/',lotto,name ='lotto_indec'),
    path('lotto/index/',lotto_index, name ='lotto_index'),
    path('lotto/result/',lotto_result, name='lotto_result')
]
