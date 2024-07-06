from django.contrib import admin
from .models import Kategori, Catatan, Tag, Komentar

admin.site.register(Kategori)
admin.site.register(Catatan)
admin.site.register(Tag)
admin.site.register(Komentar)
