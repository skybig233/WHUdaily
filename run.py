"""
@Name: run.py
@Auth: JiangZhesheng
@Date: 2022/9/12-18:54
@Desc: 每日运行脚本
"""
import os
while True:
    flag=os.system("python main.py")
    if flag==0:
        print('ok')
        break
    print("fail")