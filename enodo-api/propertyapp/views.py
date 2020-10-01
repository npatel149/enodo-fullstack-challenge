from .models import PropertyInfo
from .serializers import PropertyInfoSerializer
from rest_framework import permissions, generics


class PropertyInfoList(generics.ListCreateAPIView):
    queryset = PropertyInfo.objects.all()
    serializer_class = PropertyInfoSerializer


class PropertyInfoDetail(generics.RetrieveUpdateAPIView):
    queryset = PropertyInfo.objects.all()
    serializer_class = PropertyInfoSerializer
