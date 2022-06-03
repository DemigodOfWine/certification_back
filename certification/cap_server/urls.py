from django.urls import path
from . import views
from .views import dpc_models
from .views import dpc_models_detail
from .views import dpc_certificate_detail

urlpatterns = [
    path('', views.home_page, name='home'),
    path('search/', views.search_certificate, name='search_certificate'),
    path('print/', views.preview_certificate, name='preview_certificate'),
    path('statistics/', views.statistics, name='statistics'),
    path('dpc_models/', views.dpc_models),
    path('dpc_models_detail/<int:pk>', views.dpc_models_detail),
    path('dpc_certificate_detail/<int:pk>', views.dpc_certificate_detail),
    # path('dpc_certificate_detail_range/<int:pk>', views.dpc_certificate_detail_range),
    path('dpc_certificate_sn_range/<int:pk>/<str:stage>', views.dpc_certificate_sn_range),
    path('dpc_certificate_sn_range_preview/<int:pk>/<int:stage>/<str:sn_min>/<str:sn_max>',
         views.dpc_certificate_sn_range_preview),
    # path('dpc_certificate_sn_range_preview/<int:pk>/<str:up>/<str:down>', views.dpc_certificate_sn_range_preview),
]
