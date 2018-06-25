from django.urls import path
from . import views

app_name = 'GILTI'
urlpatterns = [
    path('', views.ClientView.as_view(), name='clientview'),
    path('sub<pk>', views.SubView.as_view(), name='subview'),
    path('sub<int:client_id>-<pk>/detail', views.SubDetail.as_view(), name='subdetail'),
    path('<int:client_id>', views.ClientDelete, name='clientdelete')
]
