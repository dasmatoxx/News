from django.db import models


class New(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(New, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.news.title
