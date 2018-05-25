#coding:utf-8
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from .models import User,Word
from django.http import JsonResponse
from .Tools import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    def check(string):
        if string.isalpha() == False:
            return False
        else:
            if len(string) < 6 or len(string) > 12 or len(string) < 6 or len(string) > 6:
                return False
            else:
                return True

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
        # print(username,password,email,nickname)\
        if check(password) == False or check(username) == False:
            return render_to_response('signup.html',{'hint':'账号或者密码不符合要求'},context_instance=RequestContext(req))
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


# 选词
def wordbook(request):
    json = {}
    username = request.COOKIES.get('username','')
    json['username'] = username
    user = User.objects.filter(username__exact=username)[0]
    json['nickname'] = user.nickname
    json['coin'] = user.coin
    json['level'] = user.level
    json['target'] = user.target
    json['word_num_today'] = user.word_num_today
    json['word_num_remember'] = user.word_num_remember
    json['day_signup'] = user.day_signup
    json['target'] = user.wordbook
    words = getWordfromBookbyGroup(json['target'])
    paginator = Paginator(words, 10)  # Show 10 words per page

    page = request.GET.get('page')
    try:
        words = paginator.page(page)
    except PageNotAnInteger:
        words = paginator.page(1)   # If page is not an integer, deliver first page.
    except EmptyPage:
        words = paginator.page(paginator.num_pages) # If page is out of range (e.g. 9999), deliver last page of results.

    json['words'] = words
    return render_to_response('wordbook.html', json)

def test(request):
    username = request.COOKIES.get('username', '')
    wordbook = getwordsfortest(username)
    return render_to_response('test.html',wordbook[0])


#学习
def study(request):
    username = request.COOKIES.get('username','')
    dict = getWordbyUser(username)
    user = User.objects.filter(username__exact=username)[0]

    if len(dict) == 0:
        json = {'error':'NoWord'}
        return render_to_response('study.html', json)


    if request.session.get(username) == None:
        request.session[username] = 0
        wordindex = 0
    else:
        wordindex = request.session[username]
        request.session[username] = (request.session[username]+0)%len(dict)

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
    json['index'] = wordindex+1
    json['total'] = len(dict)

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

def addword(request):
    username = request.COOKIES.get('username', '')
    wordname = request.GET['wordname']
    status = request.GET['status']
    print(wordname,status)
    chooseWords(username,wordname,status)
    return HttpResponse('receive')


def getNextWord(request):
    username = request.COOKIES.get('username', '')
    dict = getWordbyUser(username)

    if request.session.get(username) == None:
        request.session[username] = 0
        wordindex = 0
    else:
        wordindex = request.session[username] % len(dict)
        cmd = request.GET.get('cmd', 'default')
        # print(cmd)
        if cmd == "NEXT":
            request.session[username] = (request.session[username] + 1) % len(dict)
        else:
            request.session[username] = (request.session[username] - 1 + len(dict)) % len(dict)

    wordname = dict[wordindex][0]
    word = Word.objects.filter(wordname=wordname)[0]


    # word = Word.objects.all()[wordindex]
    wmap = {'username': username}
    wmap['total'] = str(len(dict))
    wmap['index'] = str(wordindex+1)
    # print(len(dict),wordindex)
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
    print(wmap)
    return JsonResponse(wmap, safe=False)