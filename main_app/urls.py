from django.urls import path
from.import views
from django.conf import settings


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('computers/', views.computers_index, name='index'),
  path('computers/<int:computer_id>', views.computers_detail, name='detail'),
  path('computers/create', views.ComputersCreate.as_view(), name='computers_create'),
  path('computers/<int:pk>/update', views.ComputersUpdate.as_view(), name='computers_update'),
  path('computers/<int:pk>/delete', views.ComputersDelete.as_view(), name='computers_delete'),
  path('computers/<int:computer_id>/add_comment', views.add_comment, name='add_comment'),
  path('computers/<int:computer_id>/accessories/<int:accessory_id>', views.accessories, name='accessories_add'),
  path('accessories/', views.accessories_index, name='accessory'),
  path('accessories/create', views.AccessoriesCreate.as_view(), name='accessories_create'),
  path('accessories/<int:pk>/delete', views.AccessoriesDelete.as_view(), name='accessories_delete'),
]


if settings.DEBUG:
    import debug_toolbar
    from django.urls import include
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns