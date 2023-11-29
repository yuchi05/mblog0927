from django.contrib import admin
from mysite.models import Post,Product,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date') #加上標題 網址名稱 時間

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text','pub_date')
    
admin.site.register(Post,PostAdmin)
admin.site.register(Product)
admin.site.register(Comment,CommentAdmin)