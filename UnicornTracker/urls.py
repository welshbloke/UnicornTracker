"""UnicornTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # account login urls
    url(r'^accounts/', include('accounts.urls')),

    # bug tracker urls
    url(r'^bugs/', include('bugs.urls', namespace = 'bugs', app_name='bugs')),

    # improvement tracker urls
    url(r'^improvements/', include('improvements.urls', namespace = 'improvements', app_name='improvements')),

    # paypal URLs
    url(r'^paypal/$', include('paypal.standard.ipn.urls')),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)