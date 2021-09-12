---
    layout: post
    title: "shiro框架学习"
    date: 2021-09-11 11:08:32
    categories: shiro
---


shiro 是一个功能强大和易于使用的Java安全框架，为开发人员提供一个直观而全面的解决方案的认证，授权，加密，会话管理。



* 目录
{:toc} 

# 介绍

## shiro的主要功能

+ **Authentication：** 身份认证/登录，验证用户是不是拥有相应的身份
+ **Authorization：** 授权，即权限验证，判断某个已经认证过的用户是否拥有某些权限访问某些资源，一般授权会有角色授权和权限授权；
+ **SessionManager：** 会话管理，即用户登录后就是一次会话，在没有退出之前，它的所有信息都在会话中；会话可以是普通JavaSE环境的，也可以是如Web环境的，web 环境中作用是和 HttpSession 是一样的；
+ **Cryptography：** 加密，保护数据的安全性，如密码加密存储到数据库，而不是明文存储；

## shiro 架构
+ Subject：主体，代表了当前 “用户”，这个用户不一定是一个具体的人，与当前应用交互的任何东西都Subject，如网络爬虫，机器人等；即一个抽象概念；
+ SecurityManager： 是 Shiro 的心脏；所有具体的交互都通过SecurityManager 进行拦截并控制；它管理着所有 Subject、且负责进行认证和授权、及会话、缓存的管理
+ Authenticator：认证器，负责主体认证的，即确定用户是否登录成功，我们可以使用Shiro提供的方法来认证，有可以自定义去实现，自己判断什么时候算是用户登录成功
+ Authrizer：授权器，即权限授权，给Subject分配权限，以此很好的控制用户可访问的资源
+ Realm：用于进行权限信息的验证，我们自己实现。Realm 本质上是一个特定的安全 DAO：它封装与数据源连接的细节，得到Shiro 所需的相关的数据。在配置 Shiro 的时候，必须指定至少一个Realm 来实现认证（authentication）和/或授权（authorization）。
+ SessionManager：为了可以在不同的环境下使用　session 功能，shiro 实现了自己的 sessionManager ，可以用在非 web 环境下和分布式环境下使用
+ SessionDAO：对 session 的 CURD 操作
+ CacheManager：缓存控制器，来管理如用户、角色、权限等的缓存的；
+ Cryptography：密码模块，Shiro提高了一些常见的加密组件用于如密码加密/解密的。

## 执行流程：

1. 首先调用 Subject.login(token) 进行登录，其会自动委托给 Security Manager，调用之前必须通过 SecurityUtils.setSecurityManager() 设置；
2. SecurityManager 负责真正的身份验证逻辑；它会委托给 Authenticator 进行身份验证；
3. Authenticator 才是真正的身份验证者，Shiro API中核心的身份认证入口点，此处可以自定义插入自己的实现；
4. Authenticator 可能会委托给相应的AuthenticationStrategy 进行多 Realm 身份验证，默认 ModularRealmAuthenticator 会调用 AuthenticationStrategy 进行多 Realm 身份验证；
5. Authenticator 会把相应的 token 传入 Realm，从 Realm 获取身份验证信息，如果没有返回 / 抛出异常表示身份验证失败了。此处可以配置多个 Realm，将按照相应的顺序及策略进行访问。

