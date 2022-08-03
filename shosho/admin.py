from django.contrib import admin
from .models import Post,Comment,Profile,Notification,Message,ThreadModel

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Notification)
admin.site.register(Message)
admin.site.register(ThreadModel)