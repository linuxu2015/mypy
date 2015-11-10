#!/usr/bin/env python
#_*_ coding:utf-8 _*_
##author linuxu2015@gmail.com
#脚本作用：替换指定文件中的指定字符为其他指定字符，全局替换，第一个参数搜索字符，第二个参数替换字符，第三个参数处理文件
#第四个参数是否备份
import sys,os
##判断参数是否足够，只有参数为4个或者5个的时候程序才会执行
if len(sys.argv) != 4 and len(sys.argv) != 5:
    print '''you need give 4 or 5 argument at least
    useage %s old_text new_text [-bak]''' %sys.argv[0]
else:
    old_text = sys.argv[1]
    new_text = sys.argv[2]
    filetodo = sys.argv[3]
    #将要处理文件以只读方式写入内存
    f = open(filetodo,'rb')
    ##创建备份文件
    f_bak = open('%s.bak' %filetodo,'wb')
    ##按行读取文件
    for line in f.xreadlines():
        ##将替换后的每行写入变量
        afterdo = line.replace(old_text,new_text)
        ##将内存中对象写入文件
        f_bak.write(afterdo)
        ##关闭文件
        f.close()
        f_bak.close()
    ##判断参数中是否有‘-bak’字段，有则需要备份
    if '-bak' in sys.argv:
        ##以.bak结尾的文件其实是替换之后的文件，如果需要备份，则将其修改为任意不存在的文件名，并将源文件命名为.bak，
        ##再将任意命名的新文件改名为原文件名
        os.rename('%s.bak' %filetodo , 'm')
        os.rename('%s' %filetodo,'%s.bak' %filetodo)
        os.rename('m','%s' %filetodo)

    else:
        ##如果没有.bak字段则将原文件删除，并将新文件命名为原文件名
        os.remove('%s' %filetodo)
        os.rename('%s.bak' %filetodo,'%s' %filetodo)
    
    