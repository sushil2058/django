from django.contrib import admin
from ssebs.models import post,  notice


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(post, PostAdmin)

admin.site.register(notice, NoticeAdmin)