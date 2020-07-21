---
layout: post
title: "Spring简介"
date: 2020-07-21 15:33:29
categories: Spring
---
Spring 是分层的 Java SE/EE 应用 full-stack 轻量级开源框架，以 `IoC（Inverse Of Control：反转控制）`和 `AOP（Aspect Oriented Programming：面向切面编程）`为内核，提供了展现层`Spring MVC`和持久层`Spring JDBC`以及业务层事务管理等众多的企业级应用技术，还能整合开源世界众多著名的第三方框架和类库，逐渐成为使用最多的 Java EE 企业应用开源框架.


> 什么是容器(Container): 从程序设计角度看就是封装对象的对象,因为存在放入、拿出等操作,所以容器还要管理对象的生命周期,如Tomcat就是Servlet和JSP的容器;

Spring 官网：[https://spring.io/projects/](https://spring.io/projects/)

### 1. 为什么说Spring是一个一站式的轻量级开源框架呢？
EE开发可分成三层架构，针对JavaEE的三层结构，每一层Spring都提供了不同的解决技术。
+ WEB层：SpringMVC
+ 业务层：Spring的IoC
+ 持久层：Spring的JDBCTemplate(Spring的JDBC模板，ORM模板用于整合其他的持久层框架)<br>
### 2. Spring的核心有两部分：
+ IoC：使得主业务在相互调用过程中，不用再自己维护关系了，即不用再自己创建要使用的对象了，而是由 Spring 容器统一管理，实现自动**注入**。
+ AOP：使得系统级服务得到了最大复用，且不用再手工将系统级服务混杂到主业务逻辑中了，而是由 Spring 容器统一完成**织入**。<br>
### AOP对代码进行复用
利用AOP可以对业务逻辑的各个部分进行隔离，从而使得业务逻辑各部分之间的耦合度降低，提高程序的可重用性，同时提高了开发的效率。

AOP不是一种技术，实际上是编程思想。凡是符合AOP思想的技术，都可以看成是AOP的实现

假设把应用程序想成一个立体结构的话，OOP的利刃是纵向切入系统，把系统划分为很多个模块（如：用户模块，文章模块等等），而AOP的利刃是横向切入系统，提取各个模块可能都要重复操作的部分（如：权限检查，日志记录等等）。由此可见，AOP是OOP的一个有效补充。

AOP有以下重要部分组成：
+ 关注点(每个方法调用的日志纪录...)也就是通知里面打印的内容<br>
关注点,重复代码就叫做关注点；
+ 切面    AspLog 类<br>
关注点形成的类，就叫切面(类)<br>
面向切面编程，就是指 对很多功能都有的重复的代码抽取，再在运行的时候网业务方法上动态植入“切面类代码”。
+ 切入点   addUser()<br>
执行目标对象方法，动态植入切面代码。<br>
可以通过切入点表达式，指定拦截哪些类的哪些方法； 给指定的类在运行的时候植入切面类代码

        主要的功能是：日志记录，性能统计，安全控制，事务处理，异常处理等等。

>例如：在已经开发好的项目中，给每个方法添加日志，我们的实现方式，肯定不可能是在每个方法调用的时候添加日志，因为方法很多，且都是重复代码，我们的实现实现方式是利用AOP 方式<br><br>
同理，事务的处理也是，在方法前开始事务，方法后提交事务

### 3. Spring的体系结构
![无法加载图片](https://huteng-dev.github.io/img/spring.png)<br>

核心容器由`spring-core，spring-beans，spring-context 和 spring-expression`（SpEL，Spring表达式语言，Spring Expression Language）等模块组成，它们的细节如下：

+ `spring-core`：提供了框架的基本组成部分，包括 IoC 和依赖注入功能。

+ `spring-beans`：提供 BeanFactory，工厂模式的微妙实现，它移除了编码式单例的需要，并且可以把配置和依赖从实际编码逻辑中解耦。

+ `spring-context`：模块建立在由core和 beans 模块的基础上建立起来的，它以一种类似于JNDI注册的方式访问对象。Context模块继承自Bean模块，并且添加了国际化（比如，使用资源束）、事件传播、资源加载和透明地创建上下文（比如，通过Servelet容器）等功能

+ `spring-expression`：提供了强大的表达式语言，用于在运行时查询和操作对象图。它是JSP2.1规范中定义的统一表达式语言的扩展，支持set和get属性值、属性赋值、方法调用、访问数组集合及索引的内容、逻辑算术运算、命名变量、通过名字从Spring IoC容器检索对象，还支持列表的投影、选择以及聚合等。
### 4. Spring的优点
+ 方便解耦，简化开发。<br>
Spring就是一个大工厂，可以将所有对象的创建和依赖关系的维护，交给Spring管理。

+ AOP编程的支持<br>
Spring提供面向切面编程，可以方便的实现对程序进行权限拦截、运行监控等功能。

+ 声明式事务的支持<br>
只需要通过配置就可以完成对事务的管理，而无须手动编程。

+ 方便程序的测试<br>
Spring对Junit4支持，可以通过注解方便的测试Spring程序。

+ 方便集成各种优秀的框架<br>
Spring不排斥各种优秀的开源框架，其内部提供了对各种优秀框架(如:Struts2/Hibernate/MyBatis/Quartz等)的直接支持。

+ 降低JavaEE API的使用难度<br>
Spring对JavaEE开发中非常难用的一些API(JDBC、JavaMail、远程调用等)都提供了封装，使这些API应用难度大大降低。
