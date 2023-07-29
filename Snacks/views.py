from django.shortcuts import render
from .permissions import Custoum_permissions
from .models import Snack
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import SnackSerializer
# Create your views here.

# class ThingListView(ListAPIView):
class SnackListView(ListCreateAPIView):

    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = [Custoum_permissions]
