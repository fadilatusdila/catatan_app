from rest_framework import serializers
from .models import Kategori, Catatan, Tag, Komentar

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id', 'nama']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'nama']

class CatatanSerializer(serializers.ModelSerializer):
    kategori = serializers.PrimaryKeyRelatedField(queryset=Kategori.objects.all())
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='nama'
    )
    
    class Meta:
        model = Catatan
        fields = ['id', 'judul', 'isi', 'kategori', 'tags']

class KomentarSerializer(serializers.ModelSerializer):
    catatan = serializers.PrimaryKeyRelatedField(queryset=Catatan.objects.all())
    
    class Meta:
        model = Komentar
        fields = ['id', 'catatan', 'teks', 'dibuat_pada']
