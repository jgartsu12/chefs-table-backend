from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('token-auth/', obtain_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('menus.api.urls')),
    # path('phlogapi/', include('phlogfeeder.phlogapi.urls')),
    # path('postsapi/', include('posts.postsapi.urls')),
]

if settings.DEBUG:
    # urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)