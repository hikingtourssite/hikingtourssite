"""
URL configuration for hiking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  # Import built-in auth views
from django.urls import path, include
from django.contrib.auth.views import LogoutView



# Main URL configuration
urlpatterns = [
    path('admin/', admin.site.urls),         # Admin panel
    path('', include('tours.urls')),         # Routes for the "tours" app (main page)
    
    # Built-in login and logout views
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/registration/logged_out.html'), name='logout'),

    
    # Include accounts app routes under "/accounts/"
    path('accounts/', include('accounts.urls')),

    #path('models-view/', include('django_model_viewer.urls')),

]

# Add serving of static and media files in development mode
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


