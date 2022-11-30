from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('my_example_app.urls')),
    path('admin/', admin.site.urls),
    path('', include('my_example_app.urls')),
]
