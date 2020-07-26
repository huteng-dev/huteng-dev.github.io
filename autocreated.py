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

filename0 = time.strftime("%Y-%m-%d")
realtime = time.strftime("%Y-%m-%d %H:%M:%S")
filename1 = input("请输入文件名:")
title = input("请输入标题:")
tag = input("请输入标签(使用空格隔开):")
filename = filename0+'-'+filename1+".md"
print(filename)

with open(filename, 'x', encoding='utf-8') as f:
    f.write(f'''---
layout: post
title: "{title}"
date: {realtime}
categories: {tag}
---
''')

if "_posts" in os.listdir():
    old_dir = os.getcwd()
    new_dir = os.path.join(old_dir, "_posts")
    with open(filename, 'r' ,encoding='utf-8') as f:
        content = f.read()
        with open(new_dir+'/'+filename, 'x', encoding='utf-8') as w:
            w.write(content)
    os.remove(filename)
else:
    print("Directory does not exist.")
