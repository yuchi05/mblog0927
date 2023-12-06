from django.shortcuts import render
from mysite.models import Post,Comment
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect


def homepage(request): #首頁
    posts = Post.objects.all()
    now = datetime.now()
    hour = now.timetuple().tm_hour #時間 index用到hour
    return render(request, 'index.html', locals()) #透過render呼叫網站

def showpost(request, slug):
    post = Post.objects.get(slug=slug)    #select * from post where slug=%slug
    return render(request, 'post.html', locals())

def show_all_posts(request):
    posts  = Post.objects.all()
    return render(request, 'allposts.html', locals())

def show_comments(request,post_id):
    # comments = comments.objexts.filter(post=post_id) #filter 拿多個檔案　較不適用
    comments = Post.objects.get(id=post_id).comment_set.all() #comment_set.all() 動態產生
    return render(request, 'comments.html', locals())

def carlist(request, maker=0): 
    # car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan','Toyota' ]
    # car_list = [ 
    #             [],
    #             ['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
    #             ['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
    #             ['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
    #             ['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
    #             ['Camry','Altis','Yaris','86','Prius','Vios', 'RAV4', 'Wish']
    #             ]
    car_maker = ['Ford', 'Honda', 'Mazda']
    car_list = [[ {'model':'Fiesta', 'price': 203500},
                    {'model':'Focus','price': 605000},
                    {'model':'Mustang','price': 900000}],
                [{'model':'Fit', 'price': 450000},
                    {'model':'City', 'price': 150000},
                    {'model':'NSX', 'price':1200000}],
                [{'model':'Mazda3', 'price': 329999},
                    {'model':'Mazda5', 'price': 603000},
                    {'model':'Mazda6', 'price':850000}],]
    maker = maker
    maker_name =  car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carlist.html', locals())


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
from django.http import HttpResponseRedirect
from django.urls import reverse

def new_post(request):
    print(f'form method: {request.method}') #畫網頁
    if request.method == 'GET':
        return render(request, 'myform_1.html', locals())
    elif request.method == 'POST': #透過表單的post 將網頁回傳
        title = request.POST['title']
        slug = request.POST['slug']
        content = request.POST['content']
        post=Post(title=title, slug=slug, body=content)
        post.save()
        return HttpResponseRedirect(reverse('show-all-posts')) #送出後自動導入到show-all-posts網頁 #Redirect重新導向
'''
def new_post(request):
    print(f'form method: {request.method}')
    if request.method == 'GET':
        return render(request, 'myform_1.html', locals())
    elif request.method == 'POST':
        username = request.POST['user_id']
        password = request.POST['password']
        if username == 'ntub' and password == 'a123' :
            is_validated = True
        else:
            is_validated = False
        
        print(f'post-username:{username}, password:{password}')
        return render(request, 'myform_1.html', locals())  
'''
'''
    try:
        username = request.GET['user_id']
        password = request.GET['password']
        print(f'username:{username}, password:{password}')
        return render(request, 'myform_1.html', locals())
        
    except:
        return render(request, 'myform_1.html', locals())  #如果user沒有輸入就是render , 有輸入 網址就是他輸入的值
'''
