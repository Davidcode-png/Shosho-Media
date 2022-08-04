from django.contrib import admin
from .models import Post,Comment,Profile,Notification,Message,ThreadModel,Tag

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Notification)
admin.site.register(Message)
admin.site.register(ThreadModel)
admin.site.register(Tag)