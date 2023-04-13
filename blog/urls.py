from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('blog.urls')),
    path('', views.supplement_list, name='supplement_list'),
    # path('supplement/<int:pk>/', views.supplement_detail, name='supplement_detail'),
]
