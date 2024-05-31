from django.contrib import admin
from django.urls import path
from content.views import *
from . import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',user,name='user'),
    path('register/',register,name='register'),
    path('login/',logIn,name='login'),
    path('projects/',projects,name='projects'),
    path('skills/',skills,name='skills'),
    path('tech/',tech,name='tech'),
    path('getservice/',getservice,name='getservice'),
    path('socials/',socials,name='socials'),
    path('placeorder/',placeorder,name='placeoredr'),
    path('mail/',mail,name='mail'),
    path('docs/',docs,name='docs'),
    path('education/',edu,name='education'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

