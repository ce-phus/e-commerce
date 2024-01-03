from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app/vi/auth/", include('djoser.urls')),
    path("app/v1/auth/",include("djoser.urls.jwt")),
    path('app/v1/categories/', include('apps.category.urls')),
    path('app/v1/customer/', include('apps.category.urls')),
    path('app/v1/orders/', include('apps.orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header= "Online store Admin"
admin.site.site_title= "Online Store Admin Portal"
admin.site.index_title='Welcome to the online store Portal'