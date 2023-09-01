from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    Author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def app_comments(self):
        return self.comments.filter(approved_comments=True)
    
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey('cloneApp.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')
    
    def __str__(self):
        return self.text
    
    

# Create your models here.
