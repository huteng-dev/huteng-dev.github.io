---
    layout: post
    title: "MyBatis学习"
    date: 2020-08-11 08:31:20
    categories: MyBatis
---
MyBatis 是一款优秀的持久层框架，它支持自定义 SQL、存储过程以及高级映射。MyBatis 免除了几乎所有的 JDBC 代码以及设置参数和获取结果集的工作。MyBatis 可以通过简单的 XML 或注解来配置和映射原始类型、接口和 Java POJO（Plain Old Java Objects，普通老式 Java 对象）为数据库中的记录。 

[Mybatis官方文档](https://mybatis.org/mybatis-3/zh/index.html)  


* 目录
{:toc}

## 使用
### 导入依赖
在使用SpringBoot时,如果使用的是Maven，可以直接在`pom.xml`中导入依赖
```xml
<dependency>
  <groupId>org.mybatis</groupId>
  <artifactId>mybatis</artifactId>
  <version>x.x.x</version>
</dependency>
```