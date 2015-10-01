from django.contrib import admin

from forums.models import Forum, Thread, Comment

admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(Comment)

