# -*- coding: utf-8 -*-
"""Boj4376

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YFzw46Y7lhu93jm4JTtcEzwVUel78nzm

### Boj 4376
"""

num = list(range(1,10001))

def d(n):

    a = list()

    for i in num :

        b = i + i//10 + i%10

        a.append(b)

 

    for j in num:

        if j not in a :

            print(j)