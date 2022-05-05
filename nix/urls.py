"""nix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin

from django.urls import include, path
from credito.api import views as credito
from debito.api import views as debito
from rest_framework import routers
from conta_virtual.api import views as conta
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'users', conta.UserViewSet)
router.register(r'conta', conta.ContaVirtualViewSet)
router.register(r'credito', credito.CreditoViewSet)
router.register(r'debito', debito.DebitoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('conta/<int:pk>/credito/', conta.ExtratoCredito.as_view()),
    path('conta/<int:pk>/debito/', conta.ExtratoDebito.as_view()),


    path('api-token-auth/', views.obtain_auth_token),
]