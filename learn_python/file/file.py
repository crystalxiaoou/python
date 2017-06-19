#!/usr/bin/env python
# __*__ encoding:utf-8 __*__
# def test():
#     f = None
#     try:
#         f = open('/Users/baidu/Desktop/TBL_REPAYMENT_PLAN_INFO_20170329.sql', 'r')
#         print f.read()
#
#     finally:
#         if f:
#             f.close()
#
# test()

# with open('/Users/baidu/Desktop/TBL_REPAYMENT_PLAN_INFO_20170329.sql', 'r') as f:
#     print f.read()

# 1.读取文件文件
# with open('/Users/baidu/Desktop/TBL_REPAYMENT_PLAN_INFO_20170329.sql', 'r') as f:
#     for line in f.readlines():
#         print(line.strip()) # 把末尾的'\n'删掉

# 2.读取二进制文件
# with open('/Users/baidu/Desktop/TA解决效果图.png', 'rb') as f:
#     print f.read()

# 3.写文件
with open('/Users/baidu/Desktop/test.txt', 'w') as f:
    f.write('Hello, world 2!')

with open('/Users/baidu/Desktop/test.txt', 'r') as f:
    print f.read()
    f.close