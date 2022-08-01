from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User,blank=True,related_name='likes')
    dislikes = models.ManyToManyField(User,blank=True,related_name='dislikes')

    def __str__(self) -> str:
        return f'{self.body[:20]}... {self.id}'

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User,primary_key=True,verbose_name='user',related_name='profile',on_delete=models.CASCADE)
    name = models.CharField(max_length=150,blank=True,null=True)
    bio = models.TextField(max_length=750,blank=True,null=True)
    birth_date = models.DateField(null=True,blank=True)
    location = models.CharField(max_length=150,blank=True,null=True)
    picture = models.ImageField(upload_to = 'uploads/profile_pictures',default ='uploads/profile_pictures/default.png',blank=True)
    followers = models.ManyToManyField(User,blank=True,related_name='followers')

    def __str__(self) -> str:
        return self.name.title()

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        user = instance
        Profile.objects.create(user=user,
                                name = user.username
                                )


@receiver(post_save,sender=User)
def save_user_profile(sender,instance, **kwargs):
    instance.profile.save()