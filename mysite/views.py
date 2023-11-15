from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect


def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals()) #透過render呼叫網站

def showpost(request, slug):
    post = Post.objects.get(slug=slug)    #select * from post where slug=%slug
    return render(request, 'post.html', locals())
    
# def about(request, num=-1):
#     mthml=f'''
#     <hmtl>
#     <body>
#     <h1>I</h1>
#     <h3>am in NTUB</h3>
#     <h2>{num}</h2>
#     </body>
#     </html>
#     '''
#     return HttpResponse(mthml) #直接將字串回傳給網站
import random
def about(request, num=-1): #num=-1預設值
    quotes = ['今日事，今日畢',
            '要怎麼收穫，先那麼栽',
            '知識就是力量',
            '一個人的個性就是他的命運']
    if num == -1 or num > 4:  #輸入-1或大於4 隨機挑一句話
        quote = random.choice(quotes)
    else:
        quote=quotes[num] #輸入0至3 輸出該數字那行的句子
    return render(request, 'about.html', locals())   #自動將變數包裝起來給網頁

'''
def homepage(request):  #request參數
    posts = Post.objects.all() #select * from post
    post_lists = list()
    for counter,post in enumerate(posts):
        post_lists.append(f'No. {counter} {post} <br>') #格式化
    return HttpResponse(post_lists)
'''