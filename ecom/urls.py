
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('products.urls')),
    path("",include('users.urls')),
    path("",include('seller.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)