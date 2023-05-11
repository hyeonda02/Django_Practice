from django.shortcuts import render
from django.http import HttpResponse
import random #import 파일 최상단에 위치하는게 원칙
#http모듈에 있는 HttpResponse 가져옴 

#url은 타고 뷰를 받아야됨
#url은 장고 프로젝트 폴더에 존재 (settings.py가 있는 폴더)  
#render 안에도 HttpResponse가 포함되어 있음
#html 응답하는 함수를 작성할 때에는 render 이용한다.

# Create your views here.
def calculator(reqeust): #장고가 만들어 놓은 약속 request(요청)
    #return HttpResponse("계산기 기능 구현 시작입니다.") #클래스임 import 필요하다
    print(f'reqeust = {reqeust}')
    print(f'reqeust type = {type(reqeust)}')
    
    # 1. 데이터 확인
    num1 = reqeust.GET.get('num1') # html에서 사용자가 브라우저 통해 사용자가 값을 주었을때, 값을 받는 방법
    num2 = reqeust.GET.get('num2')
    operators = reqeust.GET.get('operators')
    
    # 2. 계산
    if operators =='+' :
        result = int(num1)+int(num2)
    elif operators =='-':
        result = int(num1)-int(num2)
    elif operators =='*':
        result = int(num1)*int(num2)
    elif operators =='/':
        result =int(num1)/int(num2)
    else:
        result = 0  
    
    
    # 3. 응답   
    #html 파일에서 result 값을 result 변수로 사용 가능하다는 의미이다. 딕셔너리 이용
    return render(reqeust,'calculator.html',{'result':result}) #응답할 템플릿의 이름을 작성

def lotto(request):
    lotto_number = list()
    
    for _ in range(7):
        number = random.randint(1,45)
        lotto_number.append(number)
    return render(request,'lotto.html',{'lotto_number' : lotto_number})

def lotto_index(request):
    return render(request,'lotto_index.html')

def lotto_result(request):
    lotto_number = list()
    game = request.GET.get('game',1)
    pull_number = [index for index in range(1,46)]
    
    for _ in range(int(game)):
        lotto_number.append(random.sample(pull_number,6))
    return render(request,'lotto_result.html',{'lotto_number':lotto_number,'game':game})
    