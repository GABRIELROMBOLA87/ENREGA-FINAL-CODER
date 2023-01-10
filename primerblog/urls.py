"""primerblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from pagina.views import (index, PostListar, PostCrear,
                               PostActualizar, PostBorrar, PostDetalle,
                               UserSignUp, UserLogin, UserLogout, AvatarActualizar,
                               UserActualizar, MensajeCrear, MensajeDetalle, MensajeListar)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagina/', index, name="pagina_index" ),
    path('pagina/listar/', PostListar.as_view(), name="pagina_listar"),
    path('pagina/crear/', PostCrear.as_view(), name="pagina_crear"),
    path('pagina/<int:pk>/actualizar/', PostActualizar.as_view(), name="pagina_actualizar"),
    path('pagina/<int:pk>/borrar/', PostBorrar.as_view(), name="pagina_borrar"),
    path('pagina/<int:pk>/detalle/', PostDetalle.as_view(), name="pagina_detalle"),
    path('pagina/signup/', UserSignUp.as_view(), name="pagina_signup"),
    path('pagina/login/', UserLogin.as_view(), name="pagina_login"),
    path('pagina/logout/', UserLogout.as_view(), name="pagina_logout"),
    path('pagina/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="pagina_avatars_actualizar"),
    path('pagina/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="pagina_users_actualizar"),
    path('pagina/mensajes/crear/', MensajeCrear.as_view(), name="pagina_mensajes_crear"),
    path('pagina/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="pagina_mensajes_detalle"),
    path('pagina/mensajes/listar/', MensajeListar.as_view(), name="pagina_mensajes_listar"),
    ]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)