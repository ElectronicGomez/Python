# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 18:28:25 2020

@author: ASUS
"""
#%%
a = [1,1,0,-1,-1]
print(a)
pos = 0
neg = 0
cer =0;
x = len(a)
for i in range(x):
    if a[i]>0:
        pos+=1
    elif a[i]<0:
        neg+=1
    else:
        cer+=1
rat1= pos/x
rat2=neg/x
rat3=cer/x
#print(pos)
#print(neg)
#print(cer)
print(f'{rat1:.6f}')
print(f'{rat2:.6f}')
print(f'{rat3:.6f}')
#%%
n=5
for i in range(n):
    print(" "*(n-i-1)+"#"*(2*i+1))
#%%


        