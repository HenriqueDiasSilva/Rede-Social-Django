from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("microblogging.urls")),
    path('conta/', include('django.contrib.auth.urls'))
]