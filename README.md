# Django-ORMbasis
单表操作

        表记录的添加
             
            方式一：
             b = Book(name="python基础", price=99, author="Aaron", pub_date="2018-10-12")
             b.save()

            方式二
             Book.objects.create(name="Linux基础", price=199, author="Ping", pub_date="2019-1-12")

        表记录的修改
            方式一：
            
            b=Book.objects.get(author="Ping")
            b.price=120
            b.save()
            
            方式二：
            #update是QuerySet
            Book.objects.filter(author="Aaron").update(price=199)
         
        表记录的删除：
            Book.objects.filter(author="Lixa").delete()
            
        表记录的查询（重点）：
        
                book_list = Book.objects.filter(id=2)
                book_list=Book.objects.exclude(author="Aaron").values("name","price")
                
                book_list=Book.objects.all()
                book_list = Book.objects.all()[::2]
                book_list = Book.objects.all()[::-1]
                
                #first，last,get取到的是一个实例对象，并非一个QuerySet的集合对象
                book_list = Book.objects.first()
                book_list = Book.objects.last()  
                book_list = Book.objects.get(id=2)#只能取出一条记录时才不报错
                
                
                ret1=Book.objects.filter(author="Aaron").values("name")
                ret2=Book.objects.filter(author="Ping").values_list("name","price")
                
               

                book_list= Book.objects.all().values("name").distinct()
                book_count= Book.objects.all().values("name").distinct().count()
               
            
                模糊查询  双下划线__

                book_list=Book.objects.filter(name__icontains="P").values_list("name","price")
                book_list=Book.objects.filter(id__gt=5).values_list("name","price")
                
