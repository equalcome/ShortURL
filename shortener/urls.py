from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_short, name='create_short'),
    path('links/', views.my_links, name='my_links'),
    path('links/<str:code>/', views.link_detail, name='link_detail'),  # 詳情頁
    path('<str:code>/', views.follow, name='follow'),  # 放最後
]
