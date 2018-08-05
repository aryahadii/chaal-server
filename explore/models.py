from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=100,
                            null=False,
                            blank=False,
                            unique=True,
                            verbose_name='name')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'branches'


class Post(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=500,
                             null=False,
                             blank=False,
                             verbose_name='title')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='creation time')
    body = models.TextField(null=False, verbose_name='body')

    class Meta:
        verbose_name_plural = 'posts'
