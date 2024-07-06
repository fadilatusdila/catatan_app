from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Tag(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Catatan(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.judul

class Komentar(models.Model):
    catatan = models.ForeignKey(Catatan, on_delete=models.CASCADE)
    teks = models.TextField()
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teks
