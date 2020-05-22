# -*- coding: utf-8 -*-
'''生成指定数量的16位激活码'''
import random
import time
class activation_code(object):
    def __init__(self):
        self.listA = []
        self.str_code = ''
        self.date_list = []
    def Generate(self,num):                    #生成激活码
        for i in range(num):
            s = a = ''
            while(s in self.date_list or s == ''):
                for x in range(16):
                    a = random.choice(self.listA)
                    s = s + a
                    print(s)
            self.date_list.append(s)
        save(self.date_list)
    def Check(self,a):
        new_list = read()
        print(new_list[0])
        if a in new_list[0]:
            print("congraduation!!!!!!!!!!!")
        else:
            print("激活码错误")

def rangeSet(self, cla):
    A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    number = ['1','2','3','4','5','6','7','8','9']
    return A+a+number


def save(date):
    filename = "dateJH.txt"
    with open(filename,'w') as f:
        f.writelines(str(date))
def read():
    filename = "dateJH.txt"
    print("reading >>>>>>>>>>>>")
    rf = open(filename,'r')
    date = rf.readlines()
    return date

if __name__=="__main__":
    a = jihuoma()
 #   a.makeFW("char_h")
#    a.makeFW("char_l")
#    a.makeFW("num")
 #   a.makeJH()
#    print(a.date_list)
    a.checkJH("fDHaJklEQDRRRwa7h")

