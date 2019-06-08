from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
