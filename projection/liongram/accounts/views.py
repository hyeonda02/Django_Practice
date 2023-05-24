from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

from .forms import UserCreateForm,SignUpForm
from users.models import User


# Create your views here.

def signup_view(request):
    #GET 요청시 HTML응답
    if request.method=='GET':
        form = SignUpForm
        context ={'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        #POST 요청시 데이터 확인 후 회원 생성
        form = SignUpForm(request.POST)
        if form.is_valid():
            #회원가입 처리
            instance = form.save()
            return redirect('index')
            
        else:
            return redirect('accounts:signup')
        

def login_view(request):
    #하나하나 값을 가져와서 유효성 검사 실행 가능
    #if request.method=='GET':
    #    pass
    #else:
    #    username=request.POST.get('username')
    #    if username =='' or username ==None:
    #        pass
    #    user = User.objects.get(username==username)
    #    if user == None:
    #        pass
    #    password = request.POST.get('password')   
    
    #GET, POST 분리
    #데이터 유효성 검사
    #비지니스 로직 처리
    #응답
    if request.method=='GET':
        #로그인 HTML 응답
        return render(request, 'accounts/login.html',{'form':AuthenticationForm()})
    else:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid(): #50,51 유효성 검사
            #비지니스 로직 처리 - 로그인 처리
            login(request,form.user_cache) #비지니스 로직 처리 (로그인이 되어 있다면,)
            #응답
            return redirect('index')
            
        else:
            #비지니스 로직 처리 - 로그인 실패
            #응답
            return render(request,'accounts/login.html',{'form':form})  #출력
        
def logout_view(reqeust):
    if reqeust.user.is_authenticated:
        logout(reqeust)
    return redirect('index')