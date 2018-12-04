#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Read an integer N.

Without using any string methods, try to print the following:
123...N

Note that "" represents the values in between.
'''

print(*range(1, int(input())+1), sep='')

