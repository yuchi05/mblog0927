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
    user_name = forms.CharField(label='您的姓名', max_length=50, initial='李大仁') #CharField文字輸入 label標籤名 max_length最大值 initial預設值
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