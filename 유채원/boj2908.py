# -*- coding: utf-8 -*-
"""Boj2908

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YFzw46Y7lhu93jm4JTtcEzwVUel78nzm

### Boj 2908
"""

a,b = list(map(str,input().split()))

a = int(a[::-1])

b = int(b[::-1])

print(max(a,b))