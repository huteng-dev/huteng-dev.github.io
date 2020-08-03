import os
import time

""""
---
layout: post
title: "Spring学习笔记"
date: 2020-07-21 15:33:29
categories: Spring
---
"""

#获取现在的时间
filename0 = time.strftime("%Y-%m-%d")
realtime = time.strftime("%Y-%m-%d %H:%M:%S")
#输入参数以及创建文件名
filename1 = input("请输入文件名:")
title = input("请输入标题:")
tag = input("请输入标签(使用空格隔开):")
filename = filename0+'-'+filename1+".md"

#写入模板
if "_posts" in os.listdir():
    old_dir = os.getcwd()
    new_dir = os.path.join(old_dir, "_posts")
    with open(new_dir+'/'+filename, 'x', encoding='utf-8') as f:
        f.write(f'''---
    layout: post
    title: "{title}"
    date: {realtime}
    categories: {tag}
---
    ''')
        print("success")
else:
    print("Directory does not exist.")
