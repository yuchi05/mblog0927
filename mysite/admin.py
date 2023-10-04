from django.contrib import admin
from mysite.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date') #加上標題 網址名稱 時間
    
admin.site.register(Post,PostAdmin)