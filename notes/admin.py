from django.contrib import admin
from .models import Category, Note, Tag, Comment

admin.site.register(Category)
admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(Comment)
