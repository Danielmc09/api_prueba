from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from productos.views import ChelaViewSet, ChelaFavoritaViewSet 

router = routers.DefaultRouter()
router.register('productos', ChelaViewSet)
router.register('coupon', ChelaFavoritaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
