from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.urls import path, include
from django.conf import settings

# serving media files in DEBUG=FALSE mode, not appropriate for production
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'), # using a custom logout function
    #path('logout/', auth_views.LogoutView.as_view(template_name='users/login.html'), name='logout'),
    path('', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), # serving media files in DEBUG=FALSE mode
]
