from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

cursor = connection.cursor()

def join1(request):
    if request.method == "GET":    
        return render(request, 'member/join1.html')

def list(request):
    # ID 기준으로 오름차순
    sql = "SELECT * FROM MEMBER ORDER BY ID ASC"
    cursor.execute(sql) #sql문 실행
    data = cursor.fetchall()  # 결과값을 가져옴
    print(type(data)) # list
    print(data) #[(1,2,3,4,5),(   ),(   )]

    # list.html 을 표시하기 전에
    # list 변수에 data값을, title 변수에 "회원목록"  문자를
    return render(request, 'member/list.html', 
        {"list":data, "title": "회원목록"}) 


    

def index(request):
    #return HttpResponse("index page <hr/>")
    return render(request, 'member/index.html')

@csrf_exempt #post로 값을 전달 받는 곳은 필수
def login(request): 
    if request.method == 'GET':
        return render(request, 'member/login.html')
    elif request.method == 'POST':
        id = request.POST['id']
        pw = request.POST['pw']
        
        ar = [id, pw]
        print(ar)
    
        return redirect('/member/index')

@csrf_exempt #post로 값을 전달 받는 곳은 필수
def join(request):
    if request.method =='GET':
        return render(request, 'member/join.html')
    elif request.method == 'POST':
        id =  request.POST['id'] # html에서 넘어오는 값 받기
        na =  request.POST['name']
        ag =  request.POST['age']
        pw =  request.POST['pw']

        ar =  [id, na, ag, pw] # list로 만듬
        print(ar)

        # DB에 추가함
        sql = """
            INSERT INTO MEMBER(ID, NAME, AGE, PW, JOINDATE)
            VALUES (%s, %s, %s, %s, SYSDATE)
            """
        cursor.execute(sql, ar) 

        # 크롬에서 127.0.0.1:8000/member/index 엔터키를 자동화
        return redirect('/member/index') # /중요하다!!