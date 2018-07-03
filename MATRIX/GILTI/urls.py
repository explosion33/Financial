from django.urls import path
from . import views

app_name = 'GILTI'
urlpatterns = [
    path('', views.ClientView.as_view(), name='clientview'),
    path('sub<pk>', views.SubView.as_view(), name='subview'),
    path('sub-<pk>/detail', views.SubDetail.as_view(), name='subdetail'),
    path('<int:client_id>', views.ClientDelete, name='clientdelete'),
    path('upclient/<pk>', views.ClientUpdate.as_view(), name='updateclient'),
    path('<int:client_id>/<pk>', views.SubDelete, name='subdelete'),
    path('createclient', views.ClientCreate, name='createclient'),
    path('createsub/loc<int:client_id>', views.SubCreate, name='createsub'),
    path('updatesub/<pk>', views.SubUpdate.as_view(), name='updatesub'),
]
