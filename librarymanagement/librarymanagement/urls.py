
from django.contrib import admin
from django.urls import path
from libapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewall/',views.lib_viewe),
    path('add/',views.lib_add),
    path('view/<int:id>/', views.lib_get),
    path('update/<int:id>/',views.lib_update),
    path('delete/<int:id>/', views.lib_delete),
]
