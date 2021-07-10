from django.contrib import admin
from api.models import Post
from api.models import Comment
from api.models import Category



admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)