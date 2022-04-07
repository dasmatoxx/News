from rest_framework.generics import ListAPIView

from .models import New
from .serializers import NewsSerializer


class NewsView(ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewsSerializer
