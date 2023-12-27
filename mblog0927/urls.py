"""
URL configuration for mblog0927 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views as mv #跟from mysite.views import homepage 相等 
from mytest import views as testv

urlpatterns = [
    path('admin/', admin.site.urls), #網址後面輸入admin/至管理者介面
    path('',mv.homepage, name="homepage"),#首頁 網址後面什麼都沒輸入時預設到homepage   path('',mv.homepage) 相等
    path('post/<slug:slug>/', mv.showpost, name="showpost"), #網址名稱為在管理者內自己輸入的slug
    path('post/',mv.show_all_posts, name="show-all-posts"),
    path('post/<int:post_id>/comments', mv.show_comments, name='show-comments'), #網址後輸入post/數字／comments 出現該順序的post內留言的內容
    path('about/' , mv.about, {'num':1}), #網址後輸入about/ 出現mv內定義的資料
    path('about/<int:num>', mv.about , name='about'), #'about/<int:num>'路徑   mv.about呼叫函式     {'num':1}參數  #加入整數參數num 若在about/後輸入整數數字,網站上出現該數字
    path('post/<int:yr>/<int:mon>/<int:day>/<int:post_num>/',mv.Post, name='post-url'),
    path('carlist/',mv.carlist),
    path('carlist/<int:maker>/', mv.carlist, name='carlist-url'),
    path('post/new', mv.new_post, name="post-new"), #網址後面輸入post/new就會連到new_post
    path('test/' , testv.index, name="test-new"),
    path('test/delpost/<int:pid>', testv.delpost), #delpost垃圾桶
    path('test/contact',testv.contact, name="test-contact"),
    path('post2db', testv.post2db, name='post2db'),
    path('register/',testv.register, name='register'),
    path('login/',testv.login, name='login'),
] 