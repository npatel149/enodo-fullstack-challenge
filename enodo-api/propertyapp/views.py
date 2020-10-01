from .models import PropertyInfo
from .serializers import PropertyInfoSerializer
from rest_framework import permissions, generics
from rest_framework.filters import SearchFilter, OrderingFilter


class PropertyInfoList(generics.ListCreateAPIView):
    queryset = PropertyInfo.objects.all()
    serializer_class = PropertyInfoSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['full_address',
                     'zip',
                     'rec_type',
                     'class_description',
                     'pprior_year',
                     'town', 'city',
                     'res_type',
                     'bldg_use', ]


class PropertyInfoDetail(generics.RetrieveUpdateAPIView):
    queryset = PropertyInfo.objects.all()
    serializer_class = PropertyInfoSerializer
