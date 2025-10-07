from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='posts/', null=True, blank=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_list')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'

# Create your models here.
