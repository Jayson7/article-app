
from django.contrib import admin
from django.urls import path
import apps
from apps import views

from apps.views import HomeView, detailView, create, edit,delete, contact


urlpatterns = [
    path('admin/', admin.site.urls),
    path('/contact/', views.contact, name="contact"),
    path('/contact', views.contact, name="contact"),
    path('contact/', views.contact, name="contact"),
    path('create/', create.as_view(), name='create' ),
    path('detail/edit/<int:pk>', edit.as_view(), name="edit" ),
    path('', HomeView.as_view(), name='index' ),
    path('detail/<int:pk>', detailView.as_view(), name="detail" ),
    path('detail/<int:pk>/delete', delete.as_view(), name="delete" ),
]
