from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 200)
    body = models.TextField() #body是不限制長度的欄位
    pub_date = models.DateTimeField(auto_now_add=True) #自動取得現在時間
    
    class Meta:
        ordering = ('-pub_date', ) #反向排序(大排到小) pub_date名字需相同
    
    def __str__(self) -> str:
        return self.title
    