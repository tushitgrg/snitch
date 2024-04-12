from django.db import models
from django.contrib.auth.models import User


class imageuser(models.Model):
  relation = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
  )
  imageurl = models.CharField(max_length=200)


class Topics(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self) -> str:
    return self.name


class Message(models.Model):
  author = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
  )
  Text = models.CharField(max_length=200)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  upvotes = models.CharField(max_length=30, default='0')
  downvotes = models.CharField(max_length=30, default='0')
  updated = models.DateTimeField(auto_now=True)
  upvotedusers = models.ManyToManyField(User,
                                        related_name='upvotedusers',
                                        blank=True)
  downvotedusers = models.ManyToManyField(User,
                                          related_name='downvotedusers',
                                          blank=True)
  is_reply = models.CharField(max_length=200, default="true")

  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self) -> str:
    return self.Text[0:50]


class snitch(models.Model):
  Title = models.CharField(max_length=200)
  topics = models.ManyToManyField(
      Topics,
      related_name='topics',
      blank=True,
  )
  replies = models.ManyToManyField(Message,
                                   related_name='messages',
                                   blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  snitchtext = models.ForeignKey(
      Message,
      on_delete=models.CASCADE,
  )

  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self) -> str:
    return self.Title


# Create your models here.
