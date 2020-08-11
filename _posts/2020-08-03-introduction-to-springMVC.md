---
    layout: post
    title: "SpringMVC"
    date: 2020-08-03 11:43:42
    categories: SpringMVC
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

### @RequestMapping的其他属性

```java
/**
	 * method：限定请求方式、
	 * 		HTTP协议中的所有请求方式：
	 * 			【GET】, HEAD, 【POST】, PUT, PATCH, DELETE, OPTIONS, TRACE
	 * 		GET、POST
	 * 		method=RequestMethod.POST：只接受这种类型的请求，默认是什么都可以；
	 * 			不是规定的方式报错：4xx:都是客户端错误
	 * 				405 - Request method 'GET' not supported
	 * params：规定请求参数
	 * params 和 headers支持简单的表达式：
	 * 		param1: 表示请求必须包含名为 param1 的请求参数
	 * 			eg：params={"username"}:
	 * 				发送请求的时候必须带上一个名为username的参数；没带都会404
	 * 
	 * 		!param1: 表示请求不能包含名为 param1 的请求参数
	 * 			eg:params={"!username"}
	 * 				发送请求的时候必须不携带上一个名为username的参数；带了都会404
	 * 		param1 != value1: 表示请求包含名为 param1 的请求参数，但其值不能为 value1
	 * 			eg：params={"username!=123"}
	 * 				发送请求的时候;携带的username值必须不是123(不带username或者username不是123)
	 * 
	 * 		{“param1=value1”, “param2”}: 请求必须包含名为 param1 和param2 的两个请求参数，且 param1 参数的值必须为 value1
	 * 			eg:params={"username!=123","pwd","!age"}
	 * 				请求参数必须满足以上规则；
	 * 				请求的username不能是123，必须有pwd的值，不能有age
	 * headers：规定请求头；也和params一样能写简单的表达式
	 * 	
	 * 
	 * 
	 * consumes：只接受内容类型是哪种的请求，规定请求头中的Content-Type
	 * produces：告诉浏览器返回的内容类型是什么，给响应头中加上Content-Type:text/html;charset=utf-8
	 */
```

### @RequestMapping模糊匹配功能

```java
/**
 * URL地址可以写模糊的通配符：
 * 	？：能替代任意一个字符
 * 	*：能替代任意多个字符，和一层路径
 * 	**：能替代多层路径
 */

    //路径上可以有占位符：  占位符 语法就是可以在任意路径的地方写一个{变量名}
	//   /user/admin    /user/leifengyang
	// 路径上的占位符只能占一层路径
	@RequestMapping("/user/{id}")
	public String pathVariableTest(@PathVariable("id")String id){
		System.out.println("路径上的占位符的值"+id);
		return "success";
	}
```

---

## REST

### REST风格

REST：即 Representational State Transfer。（资源）表现层状态转化。是目前最流行的一种互联网软件架构。它结构清晰、符合标准、易于理解、扩展方便，所以正得到越来越多网站的采用
+ 资源（Resources）：网络上的一个实体，或者说是网络上的一个具体信息。
它可以是一段文本、一张图片、一首歌曲、一种服务，总之就是一个具体的存在。
可以用一个URI（统一资源定位符）指向它，每种资源对应一个特定的 URI 。
获取这个资源，访问它的URI就可以，因此 URI 即为每一个资源的独一无二的识别符。
+ 表现层（Representation）：把资源具体呈现出来的形式，叫做它的表现层（Representation）。比如，文本可以用 txt 格式表现，也可以用 HTML 格式、XML 格式、JSON 格式表现，甚至可以采用二进制格式。
+ 状态转化（State Transfer）：每发出一个请求，就代表了客户端和服务器的一次交互过程。HTTP协议，是一个无状态协议，即所有的状态都保存在服务器端。因此，如果客户端想要操作服务器，必须通过某种手段，让服务器端发生“状态转化”（State Transfer）。
而这种转化是建立在表现层之上的，所以就是 “表现层状态转化”。
+ 具体说，就是 HTTP 协议里面，四个表示操作方式的动词：GET、POST、PUT、DELETE。<br>
它们分别对应四种基本操作：GET 用来获取资源，POST 用来新建资源，PUT 用来更新资源，DELETE 用来删除资源。*资源名最好使用复数形式*

### 如何使用
```xml
<!-- 发起图书的增删改查请求；使用Rest风格的URL地址；
请求url	请求方式	表示含义
/book/1	GET：	查询1号图书
/book/1	DELETE：	删除1号图书
/book/1	PUT：	更新1号图书
/book	POST：	添加1号图书

从页面发起PUT、DELETE形式的请求?Spring提供了对Rest风格的支持
1）、SpringMVC中有一个Filter；他可以把普通的请求转化为规定形式的请求；配置这个filter;
	<filter>
		<filter-name>HiddenHttpMethodFilter</filter-name>
		<filter-class>org.springframework.web.filter.HiddenHttpMethodFilter</filter-class>
	</filter>
	<filter-mapping>
		<filter-name>HiddenHttpMethodFilter</filter-name>
		<url-pattern>/*</url-pattern>
	</filter-mapping>
2）、如何发其他形式请求？
	按照以下要求；1、创建一个post类型的表单 2、表单项中携带一个_method的参数，3、这个_method的值就是DELETE、PUT
 -->
```

*高版本Tomcat；Rest支持有点问题。如果出现405报错，解决办法是在jsp页面配置 isErrorPage="true"*

---

## 数据输出

### 如何将数据带给页面
```java
/**
 * SpringMVC除过在方法上传入原生的request和session外还能怎么样把数据带给页面
 *
 * 1）、可以在方法处传入Map、或者Model或者ModelMap。
 *      给这些参数里面保存的所有数据都会放在请求域中。可以在页面获取
 *   关系：
 *      Map，Model，ModelMap：最终都是BindingAwareModelMap在工作；
 *      相当于给BindingAwareModelMap中保存的东西都会被放在请求域中；
 *
 *      Map(interface(jdk))      Model(interface(spring)) 
 *          ||                          //
 *          ||                         //
 *          \/                        //
 *      ModelMap(clas)               //
 *                  \\              //
 *                   \\            //
 *                  ExtendedModelMap
 *                          ||
 *                          \/
 *                  BindingAwareModelMap
 *
 * 2）、方法的返回值可以变为ModelAndView类型；
 *          既包含视图信息（页面地址）也包含模型数据（给页面带的数据）；
 *          而且数据是放在请求域中；
 *          request、session、application；
 *          
 */
```

---


## SpringMVC重定向和转发

```java
/**
	 *  forward:转发到一个页面
	 *  /hello.jsp：转发当前项目下的hello；
	 *  
	 *  一定加上/，如果不加/就是相对路径。容易出问题；
	 *  forward:/hello.jsp
	 *  forward:前缀的转发，不会由我们配置的视图解析器拼串
	 * 	
     * 重定向到hello.jsp页面
	 * 有前缀的转发和重定向操作，配置的视图解析器就不会进行拼串；
	 * 
	 * 转发	forward:转发的路径
	 * 重定向	redirect:重定向的路径
	 * 		/hello.jsp:代表就是从当前项目下开始；SpringMVC会为路径自动的拼接上项目名
	 * 
	 * 		原生的Servlet重定向/路径需要加上项目名才能成功
	 * 		response.sendRedirect("/hello.jsp")
     */
```