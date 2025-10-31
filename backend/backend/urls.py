# #imp
# from django.contrib import admin
# from django.urls import path, include
# from .views import home_view 

# urlpatterns = [
#     path("", home_view, name="home"),
#     path("admin/", admin.site.urls),
#     path("api/", include("api.urls")),  # Ensure "api.urls" is included correctly
# ]

















# from .views import home_view 
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path("", home_view, name="home"),
#     path('admin/', admin.site.urls),
#     path('api/', include('api.urls')),  # Include app-level URLs
# ]

# # ✅ Serve media files during development (Not for production)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






from django.contrib import admin
from django.urls import path, include
from .views import home_view  # ✅ Ensure this is imported

urlpatterns = [
    path("", home_view, name="home"),  # ✅ Home Route
    path("admin/", admin.site.urls),  # ✅ Admin Route
    path("api/", include("api.urls")),  # ✅ Include API URLs
]

# ✅ Serve media files in development (DO NOT use this in production)
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
