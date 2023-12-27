from django import forms
from mytest import models
from mytest.models import Post

class ContactForm(forms.Form):
    
    CITY = [
        ['TP', 'Taipei'],       
        ['TY', 'Taoyuang'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['NA', 'Others'],
    ] # ['Key value','網頁顯示名稱']
    user_name = forms.CharField(label='您的姓名', max_length=50, initial='田柾國') #CharField文字輸入 label標籤名 max_length最大值 initial預設值
    user_city = forms.ChoiceField(label='居住城市', choices=CITY) #ChoiceField下拉是選單
    user_school = forms.BooleanField(label='是否在學', required=False) #BooleanField核取方塊
    user_email = forms.EmailField(label='電子郵件') #EmailField emial
    user_message = forms.CharField(label='您的意見', widget=forms.Textarea) #CharField文字輸入

'''
class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fileds = ['mood','nickname','message','del_pass']
'''

class PostForm(forms.ModelForm): #跟資料庫有關的話用modelform
    class Meta:
        model = models.Post
        fields = {'mood', 'nickname', 'message', 'del_pass'}
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '現在心情'
        self.fields['nickname'].label = '你的暱稱'
        self.fields['message'].label = '心情留言'
        self.fields['del_pass'].label = '設定密碼'
        
class UserRegisterForm(forms.Form): #跟資料庫無關 單純的表單 直接用form
    user_name = forms.CharField(label='您的姓名', max_length=50, initial='金泰亨')
    user_email = forms.EmailField(label='電子郵件')
    user_password = forms.CharField(label='輸入密碼', widget=forms.PasswordInput)
    user_password_confirm = forms.CharField(label='輸入確認密碼',widget=forms.PasswordInput)
    
class LoginForm(forms.Form):
    user_name = forms.CharField(label='您的姓名', max_length=50, initial='金泰亨')
    user_password = forms.CharField(label='輸入密碼', widget=forms.PasswordInput)