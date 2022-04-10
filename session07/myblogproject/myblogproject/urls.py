"""myblogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),   #url 패턴의 이름 = html에서 url template tag
    path('new/', views.new, name='new'),
    path('detail/<int:post_pk>', views.detail, name='detail'),
    path('edit/<int:post_pk>', views.edit, name='edit'), #경로 변수 = post_pk ; home.html의 a태그로부터 경로변수를 넘겨받는다. 따라서 post_pk값은 home.html로부터 넘겨받은 post.pk값이 된다. 그리고 detail views 실행.
    path('delete/<int:post_pk>', views.delete, name='delete'),
]


#클라이언트의 요청 -> urlconf에서 이를 수신 -> 해당하는 View를 결정. -> view에서 로직을 실행 -> 데이터베이스와 통신: Model을 통함 ->
#view가 전달받은 결과를 바탕으로 template에서 전송할 html파일 생성 -> 최종 HTML을 사용자에게 응답으로 전송