"""
URL configuration for marketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from marketplace import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="main"),
    path("tovar/<int:id>", views.tovar),
    path("korzina/", views.korzina, name="korzina"),
    path("profile/", views.profile),
    path("accounts/login/", views.user_login, name="login"),
    path("accounts/logout/", views.user_logout, name="logout"),
    path("register/", views.register),
    path("add_korzin/", views.add_korzin),
    path("del_korzin/", views.del_korzin),
    path("plus/", views.plus),
    path("minus/", views.minus),
    path("profile/", views.profile, name="profile")


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
