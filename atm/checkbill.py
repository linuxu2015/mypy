#!/usr/bin/env python
def checkbill(user):
    billfile = file('H:\\python\\mypy\\atm\\bill.log')
    for line in billfile.readlines():
        if user in line:
            print line,
