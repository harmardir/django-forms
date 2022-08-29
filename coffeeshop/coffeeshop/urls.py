from django.contrib import admin
from django.urls import path , include

from signupform.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
     path('signupform/', include('signupform.urls')),
]
