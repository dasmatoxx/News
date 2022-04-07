from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/blog/', include('applications.blog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
