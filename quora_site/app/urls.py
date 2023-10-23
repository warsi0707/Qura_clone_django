from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),

    path('add/', views.add, name='add'),
    path('addrec', views.addrec, name='addrec'),

    path('update/<int:id>/', views.update, name='update'),
    path('update/uprec/<int:id>', views.uprec, name='uprec'),

    path('delete/<int:id>/', views.delete, name='delete')



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)