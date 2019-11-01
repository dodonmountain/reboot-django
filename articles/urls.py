from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/',views.detail),
    path('<int:pk>/delete',views.delete),
    path('<int:pk>/edit',views.edit),
    path('<int:pk>/update',views.update),
]

urlpatterns += statice(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)s