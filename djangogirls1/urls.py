"""djangogirls1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include

from django.contrib import admin

#這個 urls.py 定義了全名的 URL 對應，
# 在上頭可以看到定義了 blog 前置名稱下，
# 接下來的規則是包括在 blog.urls，也就是方才在 blog 目錄中定義的 urls.py 中。

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
]
