#!/usr/bin/env python
#_*_ coding:utf-8 _*_
##author linuxu2015@gmail.com
#_*_ coding:utf-8 _*_
##author linuxu2015@gmail.com
#while True:
#import time
while True:
    print_num = int(raw_input('plz input you want print num:'))
    count = 0
    while count < 1000000000:
        count += 1
#        time.sleep(0.2)
#        print count,
#        print type(count),type(print_num),
        if count == print_num:
            print 'your num is %s' %count
            l = 1
        #    break
        elif count < print_num:
            print 'loop %d\n' %count,
            pass
        else:
            if count == print_num + 1 :
                print 'your count is %s' %print_num
                print_num = int(raw_input('plz input again you want print num:'))
                pass
            else:
                print u'�Ѿ�����'
                print_num = int(raw_input('plz input again you want print num:'))