#設定資料庫
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 200)
    body = models.TextField() #body是不限制長度的欄位
    pub_date = models.DateTimeField(auto_now_add=True) #自動取得現在時間
    
    class Meta:
        ordering = ('-pub_date', ) #將日期反向排序(大排到小) pub_date名字需相同
    
    def __str__(self) -> str:
        return self.title

class Comment(models.Model): #留言板
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #留言
    text = models.CharField(max_length=200) #文字
    pub_date = models.DateTimeField(auto_now_add=True) #時間
    
    def __str__(self):
        return self.text
    

class Product(models.Model):
    SIZES = (
        ('S', 'Small'),  #('S'->真正儲存內容, 'Small'->選項) 
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)
    result = models.BooleanField()

    