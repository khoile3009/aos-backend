from rest_framework import viewsets

from warscroll.models import Warscroll
from warscroll.serializer import WarscrollSerializer

# Create your views here.


class WarscrollViewSet(viewsets.ModelViewSet):
    queryset = Warscroll.objects.all()
    serializer_class = WarscrollSerializer
