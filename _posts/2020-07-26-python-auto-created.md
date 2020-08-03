---
layout: post
title: "Python创建一个博客模板"
date: 2020-07-26 10:27:42
categories: python Blog-template
---
因为本博客时使用jekyll搭建，每篇文章需要在"/_posts"下新建md文件，每次手动创建有点麻烦，所以使用python写了一个小脚本


模板格式大致为
```
---
layout: post
title: "Spring学习笔记"
date: 2020-07-21 15:33:29
categories: Spring
---
```
首先需要os模块（提供了非常丰富的方法用来处理文件和目录）和time模块（用于格式化日期和时间）
```python
import os
import time
```
接下来自动获取时间，以及输入的参数，在对应文件夹下面创建文件即可。
```python
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
```
[代码](https://github.com/huteng-dev/huteng-dev.github.io/blob/master/autocreated.py "emmm")