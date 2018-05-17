#coding:utf-8
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from .models import User,Word
from django.http import JsonResponse

# Create your views here.

#表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密__码',widget=forms.PasswordInput())


# 主页
def homepage(req):
    return render_to_response('homepage.html',{})


# 注册
def regist(req):
    if req.method == 'POST':
        # uf = UserForm(req.POST)
        # if uf.is_valid():
            #获取表单数据
            # username = uf.cleaned_data['username']
            # password = uf.cleaned_data['password']
        username = req.POST.get('account', 'default')
        password = req.POST.get('passwd', 'default')
        email = req.POST.get('email', 'default')
        nickname = req.POST.get('nickname', 'default')
        # print(username,password,email,nickname)

        #添加到数据库
        #User.objects.get_or_create(username = username,password = password)
        registAdd = User.objects.get_or_create(username = username,password = password,email=email,nickname=nickname)[1]
        if registAdd == False:
            #return HttpResponseRedirect('/share/')
            return render_to_response('share.html',{'registAdd':registAdd,'username':username})
        else:
            return render_to_response('share.html',{'registAdd':registAdd})


    return render_to_response('signup.html',{},context_instance=RequestContext(req))


# 登录页面
def login(req):
    if req.method == 'POST':
        #uf = UserForm(req.POST)
        #uf = UserForm(None)
        username = req.POST.get('account', 'default')
        password = req.POST.get('passwd', 'default')
        user = str(User.objects.filter(username=username).filter(password=password))
        if user != []:
            # username = uf.cleaned_data['username']
            # password = uf.cleaned_data['password']
            #对比提交的数据与数据库中的数据
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/profile/')
                #将username写入浏览器cookie，失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {}, context_instance=RequestContext(req))


# 个人主页
def profile(request):
    json = {}
    username = request.COOKIES.get('username','')
    json['username'] = username
    user = User.objects.filter(username__exact=username)[0]
    json['nickname'] = user.nickname
    json['coin'] = user.coin
    json['level'] = user.level
    json['target'] = user.target
    json['wordbook'] = user.wordbook
    json['word_num_today'] = user.word_num_today
    json['word_num_remember'] = user.word_num_remember
    json['day_signup'] = user.day_signup
    return render_to_response('profile.html', json)



#登录成功
def index(request):

    dict = Word.objects.all();
    username = request.COOKIES.get('username','')
    user = User.objects.filter(username__exact=username)[0]

    if request.session.get(username) == None:
        request.session[username] = 0
        wordindex = 0
    else:
        wordindex = request.session[username]
        request.session[username] = (request.session[username]+0)%dict.count()

    # print(wordindex)
    word = Word.objects.all()[wordindex]
    json = {'username':username}
    json['word'] = word.wordname
    json['group'] = word.group
    json['soundmark'] = word.soundmark
    json['explanation'] = word.explanation.split(";")
    json['demo_1'] = word.demo_1
    json['demo_1_translate'] = word.demo_1_translate
    json['demo_2'] = word.demo_2
    json['demo_2_translate'] = word.demo_2_translate
    json['demo_3'] = word.demo_3
    json['demo_3_translate'] = word.demo_3_translate
    json['nickname'] = user.nickname

    # print(json)

    return render_to_response('study.html', json)

#退出登录

def logout(req):
    response = HttpResponse('logout!!!')
    #清除cookie里保存的username
    response.delete_cookie('username')
    return response


def share(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            return render_to_response('share.html',{'username':username})
    else:
        uf = UserForm()
    return render_to_response('share.html',{'uf':uf})

a = [1,2,3,4,5]
def ajax_list(request):
    username = request.COOKIES.get('username', '')
    print(username)
    if request.session.get(username) == None:
        request.session[username] = 0
        return JsonResponse([a[0]], safe=False)
    else:
        request.session[username] += 1
        i = request.session[username]
        return JsonResponse([a[i%5]], safe=False)

def getNextWord(request):
    dict = Word.objects.all();

    username = request.COOKIES.get('username', '')
    if request.session.get(username) == None:
        request.session[username] = 0
        wordindex = 0
    else:
        wordindex = request.session[username]
        cmd = request.GET.get('cmd', 'default')
        if cmd == "NEXT":
            request.session[username] = (request.session[username] + 1) % dict.count()
        else:
            request.session[username] = (request.session[username] - 1 + dict.count()) % dict.count()


    # print(wordindex)

    word = Word.objects.all()[wordindex]
    wmap = {'username': username}
    wmap['word'] = word.wordname
    wmap['group'] = word.group
    wmap['soundmark'] = word.soundmark
    wmap['explanation'] = word.explanation
    wmap['demo_1'] = word.demo_1
    wmap['demo_1_translate'] = word.demo_1_translate
    wmap['demo_2'] = word.demo_2
    wmap['demo_2_translate'] = word.demo_2_translate
    wmap['demo_3'] = word.demo_3
    wmap['demo_3_translate'] = word.demo_3_translate
    return JsonResponse(wmap, safe=False)