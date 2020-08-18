
from django.contrib import admin
from django.urls import path, include
from homepage import views
from django_email_verification import urls as mail_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('email/', include(mail_urls)),
]
