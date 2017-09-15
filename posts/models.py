from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(Profile)
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=100, default="")
    text = RichTextField(default="")
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title) + " - " + str(self.author)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(default="")
    comment_owner = models.CharField(max_length=30)
    comment_date = models.DateTimeField('date commented')

    def __str__(self):
        return self.comment_owner + " - " + str(self.comment_date)


class SubComment(models.Model):
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    subcomment = models.TextField(default="")
    subcomment_owner = models.CharField(max_length=30)
    comment_date = models.DateTimeField('date commented')


