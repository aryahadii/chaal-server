from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='creation time'
    )
    modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name='modified time'
    )

    class Meta:
        abstract = True


class Subchaal(TimeStampedModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='name'
    )

    class Meta:
        verbose_name_plural = 'subchaals'


class Thread(TimeStampedModel):
    title = models.CharField(max_length=64)
    subchaal = models.ForeignKey(Subchaal, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'threads'


class Post(TimeStampedModel):
    thread = models.ForeignKey(Thread, on_delete=models.DO_NOTHING)
    parent_post = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        null=True
    )

    title = models.CharField(max_length=500, verbose_name='title')
    body = models.TextField(verbose_name='body')

    class Meta:
        verbose_name_plural = 'posts'
