from django.db import models

# modellerimizi buradan yaratiyoruz
# blog yazilarimiz icin model olusturalim


class Post(models.Model):
    # basligi 100 karakterle sınırladık
    title = models.CharField(max_length=100)
    # alt metini 100 karakterle sınırladık
    subtitle = models.CharField(max_length=100)
    content = models.TextField()  # iceriklerimiz yazi alanı kullanacak
    author = models.ForeignKey(  # coktan tekile ilişki ( bir kullanıcı bir çok içerik üretebilir)
        'auth.User',  # django tarafından oluşturulmuş kullanıcı bilgisi
        on_delete=models.CASCADE,  # olusturan kullanıcı silme islemi gerceklestirebilir
    )
    # postun olusturuldugu tarih eklemesi
    date = models.DateTimeField(auto_now_add=True)

    # modele admin panelinden image ekleme secenegi ve default directory belirlemek
    image = models.ImageField(upload_to='images/', null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
