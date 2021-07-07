---
    layout: post
    title: "MyBatis学习"
    date: 2021-06-11 08:31:20
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

### 环境搭建

1. 创建maven工程并导入坐标
2. 创建实体类和dao的接口
3. 在application.yml中设置Mybatis基础配置
4. 创建映射配置文件 XXXDao.xml（用来实现某个的SQL语句）

但是需要注意
```
mybatis的映射配置文件位置必须和dao接口的包结构相同
映射配置文件的mapper标签namespace属性的取值必须是dao接口的全限定类名
映射配置文件的操作配置（select）,id属性的取值必须是dao接口的方法名
创建的实体类中的成员变量名应与数据库中的表头一致(也可使用resultMap对变量名进行匹配)。
```

### 方法
在使用Mybatis中，有两种开发方式，一种是基于XML文档，另一种是基于注解。
+ 基于注解
```java
public interface UserDao {
    @Select("select * from user")
    List<User> findAll();
}
```
+ 基于XML文档
```xml
<mapper namespace="dao.UserDao">
    <!--查询user表中的所有信息 -->
    <select id="findAll" resultType="model.User">
        select * from user
    </select>
</mapper>
```

XML文档基础模板
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="（在此处写自己的dao接口全路径）">
（在这里编写动态sql语句）
</mapper>
```

## 注意事项
在Mybatis书写动态SQL语句时，有两种拼接语句的方式一个是`#{}`（占位符），另一个是`${}`（拼接符）。前者是先将sql语句匹配处替换为？，然后类似于下面这种方法来安全设置值，可以比较有效的防止sql注入
```java
PreparedStatement ps = conn.prepareStatement(sql);
ps.setInt(1,id);
```
而拼接符则是直接讲传递来的参数直接拼接到SQL语句上，安全性较差，但是比如在使用order by等字段时，必须要使用`${}`.这种类型的字段最好不让用户自己输入。其拼接方式类似于下面的代码。
```java
Statement st = conn.createStatement();  
ResultSet rs = st.executeQuery(sql);
```