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


## SpringMVC

###  概述

1. Spring 为展现层提供的基于 MVC 设计理念的优秀的 Web 框架，是目前最主流的 MVC 框架之一。
2. Spring3.0 后全面超越 Struts2，成为最优秀的 MVC 框架。
3. Spring MVC 通过一套 MVC 注解，让 POJO 成为处理请求的控制器，而无须实现任何接口。
4. 支持 REST 风格的 URL 请求。
5. 采用了松散耦合可插拔组件结构，比其他 MVC 框架更具扩展性和灵活性。

### SpringMVC的MVC实现思想

![无法加载图片](https://huteng-dev.github.io/img/springmvc.png)

---

## hello world

### 流程

1. 导包

```
commons-logging-1.1.3.jar
spring-aop-4.0.0.RELEASE.jar
spring-beans-4.0.0.RELEASE.jar
spring-context-4.0.0.RELEASE.jar
spring-core-4.0.0.RELEASE.jar
spring-expression-4.0.0.RELEASE.jar
spring-web-4.0.0.RELEASE.jar
spring-webmvc-4.0.0.RELEASE.jar
```

2. 写配置

+ web.xml,配置springmvc的前端控制器，指定springmvc配置文件位置
```xml
<!-- The front controller of this Spring Web application, responsible for
        handling all application requests -->
    <servlet>
        <servlet-name>springDispatcherServlet</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>classpath:springmvc.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>

    <!-- Map all requests to the DispatcherServlet for handling -->
    <servlet-mapping>
        <servlet-name>springDispatcherServlet</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
```

+ 框架自身

```xml
<context:component-scan base-package="com.atguigu"></context:component-scan>
    <!-- 视图解析器，可以简化方法的返回值，返回值就是作为目标页面地址，
        只不过视图解析器可以帮我们拼串
     -->
     <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/pages/"></property>
        <property name="suffix" value=".jsp"></property>
     </bean>
```

3. 测试

```java
@Controller
public class MyFirstController {

    @RequestMapping("/hello")
    public String myfirstRequest(){
        System.out.println("请求收到了....正在处理");

        return "success";
    }
```

### 细节

+ 运行流程
    + 客户端点击链接会发送http://localhost:8080/SpringMVC_war_exploded/hello 请求
    + 来到tomcat服务器；
    + SpringMVC的前端控制器收到所有请求；
    + 来看请求地址和@RequestMapping标注的哪个匹配，来找到到底使用那个类的哪个方法来处理
    + 前端控制器找到了目标处理器类和目标方法，直接利用返回执行目标方法；
    + 方法执行完成以后会有一个返回值；SpringMVC认为这个返回值就是要去的页面地址
    + 拿到方法返回值以后；用视图解析器进行拼串得到完整的页面地址；
    + 拿到页面地址，前端控制器帮我们转发到页面；

    **一个方法处理一个请求**

+ @RequestMapping
    + 就是告诉SpringMVC；这个方法用来处理什么请求；这个/是可以省略，即使省略了，也是默认从当前项目下开始；
+ 在web.xml中如果不指定配置文件位置
    + 如果不指定也会默认去找一个文件；/WEB-INF/xxx-servlet.xml

```xml
<!-- 
        /：拦截所有请求，不拦截jsp页面，*.jsp请求
        /*：拦截所有请求，拦截jsp页面，*.jsp请求            
        处理*.jsp是tomcat做的事；所有项目的小web.xml都是继承于大web.xml
        DefaultServlet是Tomcat中处理静态资源的？
            除过jsp，和servlet外剩下的都是静态资源；
            index.html：静态资源，tomcat就会在服务器下找到这个资源并返回;
            我们前端控制器的/禁用了tomcat服务器中的DefaultServlet          
        
        1）服务器的大web.xml中有一个DefaultServlet是url-pattern=/
        2）我们的配置中前端控制器 url-pattern=/
                静态资源会来到DispatcherServlet（前端控制器）看那个方法的RequestMapping是这个index.html
        3）为什么jsp又能访问；因为我们没有覆盖服务器中的JspServlet的配置
        4） /*  直接就是拦截所有请求；我们写/；也是为了迎合后来Rest风格的URL地址
    -->
```