from rest_framework.urlpatterns import format_suffix_patterns
from propertyapp import views
from django.urls import path

urlpatterns = [
    path('', views.PropertyInfoList.as_view(), name='property-info-list'),
    path('<int:pk>/', views.PropertyInfoDetail.as_view(), name='property-info-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
