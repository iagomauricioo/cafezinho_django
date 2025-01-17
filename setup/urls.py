from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from cafezinho.views import ContribuicaoViewSet, ContribuinteViewSet

router = routers.DefaultRouter()
router.register(r"contribuintes", ContribuinteViewSet)
router.register(r"contribuicoes", ContribuicaoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls))
]
