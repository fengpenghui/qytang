#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923


department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

line1 = 'Department1  name:{0:<10}  depart1_m:{1:<10}  COURSE_FEES_SEC:{2:<10.6f}   The End!'.format(department1,depart1_m,COURSE_FEES_SEC)
line2 = 'Department2  name:{0:<10}  depart2_m:{1:<10}  COURSE_FEES_Python:{2:<10.2f}   The End!'.format(department2,depart2_m,COURSE_FEES_Python)

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)
