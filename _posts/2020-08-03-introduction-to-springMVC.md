---
    layout: post
    title: "SpringMVC"
    date: 2020-08-03 11:43:42
    categories: Spring SpringMVC
---
SpringMVC是一种轻量级的、基于MVC的Web层应用框架。偏前端而不是基于业务逻辑层。是Spring框架的一个后续产品。


* 目录
{:toc}

## MVC模式
MVC 模式代表 Model-View-Controller（模型-视图-控制器）模式。这种模式用于应用程序的分层开发。
+ Model（模型） - 模型代表一个存取数据的对象或 JAVA POJO。它也可以带有逻辑，在数据变化时更新控制器。
+ View（视图）  - 视图代表模型包含的数据的可视化。
+ Controller（控制器） - 控制器作用于模型和视图上。它控制数据流向模型对象，并在数据变化时更新视图。它使视图与模型分离开。


## SpringMVC 概述

1. Spring 为展现层提供的基于 MVC 设计理念的优秀的 Web 框架，是目前最主流的 MVC 框架之一。
2. Spring3.0 后全面超越 Struts2，成为最优秀的 MVC 框架。
3. Spring MVC 通过一套 MVC 注解，让 POJO 成为处理请求的控制器，而无须实现任何接口。
4. 支持 REST 风格的 URL 请求。
5. 采用了松散耦合可插拔组件结构，比其他 MVC 框架更具扩展性和灵活性。

### SpringMVC的MVC实现思想

![无法加载图片](https://huteng-dev.github.io/img/springmvc.png)
