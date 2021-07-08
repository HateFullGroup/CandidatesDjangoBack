"""CandidatesDjangoBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import patterns as patterns
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.static import serve
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from CandidatesDjangoBack.settings import MEDIA_ROOT, STATIC_ROOT, DEBUG
urlpatterns = [
    # App
    # path('', admin.site.urls),
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include('candidates.urls'), name='api'),
    # path('api/user/', include('users.urls')),

    # Auth
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Heroku

    url(r'^media/(?P<path>.*)$', serve,{'document_root':  MEDIA_ROOT}, name='media'),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': STATIC_ROOT}, name='static'),
]

# if DEBUG:
#   urlpatterns += patterns("",
#     url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root':MEDIA_ROOT}, name='debug_media')
# )

# urlpatterns += staticfiles_urlpatterns()