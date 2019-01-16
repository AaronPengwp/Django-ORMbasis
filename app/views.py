from django.shortcuts import render, HttpResponse
from app.models import *


# Create your views here.


def index(request):
    return render(request, 'index.html')


def addbook(request):
    # 方式一
    # b = Book(name="python基础", price=99, author="Aaron", pub_date="2018-10-12")
    # b.save()

    # 方式二
    # Book.objects.create(name="Linux基础", price=199, author="Ping", pub_date="2019-1-12")
    # Book.objects.create(**dic)

    return HttpResponse("添加成功")


def update(request):
    # Book.objects.filter(author="Aaron").update(price=200)

    b = Book.objects.get(author="Ping")
    b.price = 50
    b.save()
    print(b)
    print(type(b))
    return HttpResponse("更新成功")


def delete(request):
    Book.objects.filter(author="Lixa").delete()

    return HttpResponse("删除成功")


def select(request):
    # book_list = Book.objects.all()
    # print(book_list)  # QuerySet 集合
    # print(book_list[0])  # Book object

    # book_list = Book.objects.filter(id=2)
    # book_list = Book.objects.all()[:3]
    # book_list = Book.objects.all()[::2]
    book_list = Book.objects.all()[::-1]

    # first，last,get取到的是一个实例对象，并非一个QuerySet的集合对象
    # ret = Book.objects.first()
    # ret = Book.objects.last()
    # print(ret)
    # book_list = Book.objects.get(id=2)  # 只能取出一条记录时才不报错

    # ret = Book.objects.filter(author="Aaron").values("name")  # <QuerySet [{'name': 'python基础'}, {'name': 'PHP'}]>
    # ret = Book.objects.filter(author="Aaron").values("name","price")  # <QuerySet [{'name': 'python基础', 'price': 200}, {'name': 'PHP', 'price': 33}]>
    # ret = Book.objects.filter(author="Aaron").values_list("name","price")  # 以列表的形式显示
    #
    # print(ret)

    # book_list = Book.objects.all().values("name").distinct() #去重复
    # book_count = Book.objects.all().values("name").distinct().count()
    # print(book_count)
    # 万能的双下划线__
    book_list = Book.objects.filter(price__gte=50).values("name", "price")
    # 模糊查询
    book_list = Book.objects.filter(name__contains="P").values("name", "price")
    book_list = Book.objects.filter(name__icontains="P").values("name", "price")  # 不区分大小写

    return render(request, "index.html", {"book_list": book_list})
