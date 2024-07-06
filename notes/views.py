from rest_framework import viewsets
from .models import Kategori, Catatan, Tag, Komentar
from .serializers import KategoriSerializer, CatatanSerializer, TagSerializer, KomentarSerializer

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class CatatanViewSet(viewsets.ModelViewSet):
    queryset = Catatan.objects.all()
    serializer_class = CatatanSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class KomentarViewSet(viewsets.ModelViewSet):
    queryset = Komentar.objects.all()
    serializer_class = KomentarSerializer
