from django.contrib import admin
from .models import Islands,Bbs,Note,Bbs_content,Note_content

admin.site.register(Islands)
admin.site.register(Bbs)
admin.site.register(Note)
admin.site.register(Bbs_content)
admin.site.register(Note_content)