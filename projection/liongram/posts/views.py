from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from .models import Post
from .forms import PostBaseForm, PostCreateForm
# Create your views here.
def index(request):
    post_list=Post.objects.all().order_by('-created_at')
    context={
        'post_list':post_list,
    }
    return render(request, 'index.html',context)

def post_list_view(request):
    post_list=Post.objects.all()
    #post_list=Post.objects.filter(writer=request.user) #Post.writer가 현재 로그인 한 것만 조회
    context={
        'post_list':post_list,
    }
    return render(request, 'posts/post_list.html',context)

@login_required(login_url='/accounts/login/')
def post_detail_view(request,id):
    if request.method=='GET':
        try:
            post=Post.objects.get(id=id)
        except Post.DoesNotExist:
            return redirect('index')
        context={
            'post':post
        }
        return render(request, 'posts/post_detail.html',context)
            

@login_required
def post_create_view(request):
    if request.method=='GET':
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content=content,
            writer=request.user
        )
        return redirect('index')
    
def post_create_form_view(request):
    if request.method=='GET':
        form = PostBaseForm()
        context = {'form':form}
        return render(request, 'posts/post_form2.html',context)
    else:
        form = PostBaseForm(request.POST,request.FILES)
        if form.is_valid():
            Post.objects.create(
                #폼에서는 유효성 처리와 후처리를 수행해줌
                #cleaneddata는 유효성 처리를 해줌 (폼에 작성한 것을 기반으로 유효성 검사 실행)
                image=form.cleaned_data['image'],
                content=form.cleaned_data['content'],
                writer=request.user,
            )
        else:
            return redirect('posts:post-create')
        return redirect('index')

def post_update_view(request,id):
    #post = Post.objects.get(id=id)
    post=get_object_or_404(Post,id=id,writer=request.user)
    if request.method=='GET':
        return render(request, 'posts/post_form.html')
    elif request.method=='POST':
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        
        print(new_image)
        print(content)
        
        if new_image:
            post.image.delete()
            post.image=new_image
            
        post.content=content
        post.save()
        return redirect('posts:post-detail',post.id)
@login_required
def post_delete_view(request,id):
    post=get_object_or_404(Post,id=id)
    #if request.user !=post.writer:
    #   return Http404('잘못된 접근입니다.') 
    if request.method=='GET':
        context={'post':post}
        return render(request, 'posts/post_confirm_delete.html',context)
    else:
        post.delete()
        return redirect('index')











#응답 방법
# 함수 기반 뷰 (클래스가 없음)
def url_view(request):
    print('url_view()')
    data = {'code':'001','msg':'OK'}
    return HttpResponse("<h1>url_view</h1>")
    #return JsonResponse(data)
    
#데이터를 받는 방법
def url_parameter_view(request,username):
    print('url_parameter_view()')
    print(f'username:{username}')
    print(f'request.GET:{request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    
    if request.method == 'GET':
        print(f'request.GET:{request.GET}')
        
    elif request.method == 'POST':
        print(f'request.POST:{request.POST}')
    
    return render(request,'view.html')

def function_list_view(request):
    object_list=Post.objects.all().order_by('-id')
    return render(request,'cbv_view.html',{'object_list':object_list})
    
#클래스 기반 뷰 cbv
class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'

