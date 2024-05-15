from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from rest_framework import routers

from feedback import views

router = routers.DefaultRouter()
router.register(r'cars', views.CarModelViewSet)
router.register(r'feedbacks', views.FeedBackViewSet)


urlpatterns = [
    path('', RedirectView.as_view(url='/api')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),

]
