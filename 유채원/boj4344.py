# -*- coding: utf-8 -*-
"""Boj4344

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YFzw46Y7lhu93jm4JTtcEzwVUel78nzm

### Boj 4344
"""

t = int(input())

 
for i in range(t) :

    l = list()

    a = list(map(int,input().split()))

    for j in range(len(a)-1) :

        

        if a[j+1] > ((sum(a)-a[0])/(len(a)-1)) :

            l.append(a[j+1])

        else :

            pass

    print('%.3f%%' % ((len(l)/(len(a)-1))*100))