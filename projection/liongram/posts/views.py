from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.generic import ListView
from .models import Post
# Create your views here.
def index(request):
    return render(request, 'index.html')

def post_list_view(request):
    return render(request, 'posts/post_list.html')

def post_detail_view(request,id):
    return render(request, 'posts/post_detail.html')

def post_create_view(request):
    return render(request, 'posts/post_form.html')

def post_update_view(request,id):
    return render(request, 'posts/post_form.html')

def post_delete_view(request,id):
    return render(request, 'posts/post_confirm_delete.html')

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

