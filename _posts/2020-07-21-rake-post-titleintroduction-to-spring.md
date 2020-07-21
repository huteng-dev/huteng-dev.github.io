---
layout: post
title: "Spring简介"
date: 2020-07-21 15:33:29
categories: Spring
---
## Spring简介
Spring 是分层的 Java SE/EE 应用 full-stack 轻量级开源框架，以 `IoC（Inverse Of Control：反转控制）`和 `AOP（Aspect Oriented Programming：面向切面编程）`为内核，提供了展现层`Spring MVC`和持久层`Spring JDBC`以及业务层事务管理等众多的企业级应用技术，还能整合开源世界众多著名的第三方框架和类库，逐渐成为使用最多的 Java EE 企业应用开源框架.
> 什么是容器(Container): 从程序设计角度看就是封装对象的对象,因为存在放入、拿出等操作,所以容器还要管理对象的生命周期,如Tomcat就是Servlet和JSP的容器;

Spring 官网：[https://spring.io/projects/](https://spring.io/projects/)

### 1.为什么说Spring是一个一站式的轻量级开源框架呢？
EE开发可分成三层架构，针对JavaEE的三层结构，每一层Spring都提供了不同的解决技术。
+ WEB层：SpringMVC
+ 业务层：Spring的IoC
+ 持久层：Spring的JDBCTemplate(Spring的JDBC模板，ORM模板用于整合其他的持久层框架)
### Spring的核心有两部分：
+ IoC：使得主业务在相互调用过程中，不用再自己维护关系了，即不用再自己创建要使用的对象了，而是由 Spring 容器统一管理，实现自动**注入**。
+ AOP：使得系统级服务得到了最大复用，且不用再手工将系统级服务混杂到主业务逻辑中了，而是由 Spring 容器统一完成**织入**。
