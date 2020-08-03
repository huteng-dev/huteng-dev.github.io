---
layout: post
title: "Spring学习笔记"
date: 2020-07-22 09:33:29
categories: Spring IOC AOP
---

Spring 是分层的 Java SE/EE 应用 full-stack 轻量级开源框架，以 `IOC（Inverse Of Control：反转控制）`和 `AOP（Aspect Oriented Programming：面向切面编程）`为内核，提供了展现层`Spring MVC`和持久层`Spring JDBC`以及业务层事务管理等众多的企业级应用技术，还能整合开源世界众多著名的第三方框架和类库，逐渐成为使用最多的 Java EE 企业应用开源框架.


* 目录
{:toc}

## Spring简介
### 1. 为什么说Spring是一个一站式的轻量级开源框架呢？
EE开发可分成三层架构，针对JavaEE的三层结构，每一层Spring都提供了不同的解决技术。
+ WEB层：SpringMVC
+ 业务层：Spring的IOC
+ 持久层：Spring的JDBCTemplate(Spring的JDBC模板，ORM模板用于整合其他的持久层框架)

### 2. Spring的核心有两部分：
+ IOC：使得主业务在相互调用过程中，不用再自己维护关系了，即不用再自己创建要使用的对象了，而是由 Spring 容器统一管理，实现自动**注入**。
+ AOP：使得系统级服务得到了最大复用，且不用再手工将系统级服务混杂到主业务逻辑中了，而是由 Spring 容器统一完成**织入**。<br>

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


Spring 官网：[https://spring.io/projects/](https://spring.io/projects/)

---
## IOC介绍

Spring（IOC+AOP）

![无法加载图片](https://huteng-dev.github.io/img/spring-ioc-aop.png)


+ IOC: (Inversion(反转) Of Control)：控制反转
    + 控制:资源的获取方式
        + 主动式：(需要什么资源自己创建即可)<br>
            ```java
            BookServlet{
                BookService bs = new BookService();
                //但是复杂对象的创建是比较麻烦的
            }
            ```
        + 被动式：资源的获取不是我们自己创建的，而是交给一个容器来创建和设置
            ```java
            BookServlet{
                BookServlet bs;
                public void test01(){
                    bs.checkout();
                }
            }
            ```
    + 容器：管理所有的组件（有功能的类）（假设BookServlet和BookService都受容器管理；容器可以自动的探查出哪些组件（类）用到另一些组件（类）；容器帮我们创建BookService对象，并把BookService对象赋值过去。

    容器：主动的new资源变为被动的接受资源


IOC是一种思想，DI是对这种思想的描述


DI（Dependency Injection）依赖注入：<br>
容器能知道哪个组件（类）需要用到用到另一个组件（类），容器通过反射的形式，将容器中准备好的Bookservice对象注入（*利用反射给属性赋值*）到BookService

只要是容器管理的组件，都能使用容器提供的强大功能

### Spring的注解
```
Spring有四个注解:

@Controller:控制器;给控制器层(servlet包 下的这些)的组件加这个注解
@Service:业务逻辑;给业务逻辑层的组件添加这个注解; 
@Repository:给数据库层(持久化层，dao层)的组件添加这个注解
@Component:给不属于以上几层的组件添加这个注解;
```
*注解可以随便加，Spring底层不会去验证你的这个组件，是否如你注解所说就是一个dao层的或者就是一个servlet层的组件,主要是给程序员看了好理解。*


+ `@Autowired`:注解实现根据类型进行自动装配（最强大，Spring自己的注解）
+ `@Resource`:也可实现自动装配;j2ee,java的标准。(拓展性更强.因为是java的标准，所以如果使用另外一个容器框架@Resource仍可使用)
+ `@Qualifier`:指定一个名作为id, 让spring别使用变量名作为id

@Autowired原理:
+ 先按照类型去容器中找到对应的组件; (*xxx = ioc.getBean(xxx.class)*)
    + 找到一个:找到就赋值
    + 没找到? 抛异常
    + 找到多个? 装配上?
        + 按照变量名作为id继续匹配;
            + 匹配上? 装配
            + 没有匹配上? 报错
                （原因：因为按照变量名作为id继续匹配）使用@Qualifier指定一个字符串作为新的id
                [找到? 装配；没有找到? 报错]

@Autowired默认为一定可以装配上，使用`@Autowired(required=false)`在装配不上时，赋值为null

使用Spring的单元测试;
+ 导包; Spring单元测试包spring-test-4.0.0. RELEASE.jar
+ @ContextConfiguration(locations="" )使用它来指定Spring的配置文件的位置
+ @RunWith指定用哪种驱动进行单元测试，默认就是junit
    @RunWith(SpringJUnit4ClassRunner.class)<br>
    使用Spring的单元测试模块来执行标了@Test注解的测试方法;<br>
    以前@Test注解只是由junit执行

好处:我们不用ioc.getBean ()获取组件了;直接Autowired组件。Spring为我们自动装配

### IOC操作步骤
1. 导包

```
核心容器
spring-beans-4.0.0.RELEASE.jar
spring-context-4.0.0.RELEASE.jar
spring-core-4.0.0.RELEASE.jar
spring-expression-4.0.0.RELEASE.jar
commons-logging-1.1.3.jar
Spring运行的时候依赖一个日志包；没有就报错；
```

2. 写配置
 spring的配置文件中，集合了spring的ioc容器管理的所有组件（会员清单）；
     创建一个Spring Bean Configuration File（Spring的bean配置文件）；

```xml
<!-- 注册一个Person对象，Spring会自动创建这个Person对象 -->
    <!--
    一个Bean标签可以注册一个组件（对象、类） 
    class：写要注册的组件的全类名
    id：这个对象的唯一标示；
    -->
    <bean id="person01" class="com.atguigu.bean.Person">
        <!--使用property标签为Person对象的属性赋值 
            name="lastName"：指定属性名
            value="张三"：为这个属性赋值
        -->
        <property name="lastName" value="张三"></property>
        <property name="age" value="18"></property>
        <property name="email" value="zhangsan@atguigu.com"></property>
        <property name="gender" value="男"></property>
    </bean>
```

3. 测试

```java
@Test
    public void test() {
        //ApplicationContext：代表ioc容器
        //ClassPathXmlApplicationContext:当前应用的xml配置文件在 ClassPath下
        //根据spring的配置文件得到ioc容器对象
        ApplicationContext ioc = new ClassPathXmlApplicationContext("ioc.xml");
        
        //容器帮我们创建好对象了；
        Person bean = (Person) ioc.getBean("person01");
        
        System.out.println(bean);
        
    }
```

### 问题及细节

```java
/**
     * 存在的几个问题；
     * 1）、src，源码包开始的路径，称为类路径的开始；
     *      所有源码包里面的东西都会被合并放在类路径里面；
     *      java：/bin/
     *      web：/WEB-INF/classes/
     * 2）、导包commons-logging-1.1.3.jar（依赖）
     * 3）、先导包再创建配置文件；
     * 4）、Spring的容器接管了标志了s的类；
     */
    /**
     * 几个细节：
     * 1）、ApplicationContext（IOC容器的接口）
     * 2）、Q:给容器中注册一个组件；我们也从容器中按照id拿到了这个组件的对象？
     *      A:组件的创建工作，是容器完成；
     *      Q:Person对象是什么时候创建好了呢？
     *      A:容器中对象的创建在容器创建完成的时候就已经创建好了；
     * 3）、同一个组件在ioc容器中是单实例的；容器启动完成都已经创建准备好的；
     * 4）、容器中如果没有这个组件，获取组件？报异常
     * org.springframework.beans.factory.NoSuchBeanDefinitionException:
     * No bean named 'person' is defined
     * 5）、ioc容器在创建这个组件对象的时候，(property)会利用setter方法为javaBean的属性进行赋值；
     * 6）、javaBean的属性名是由什么决定的？getter/setter方法是属性名;set去掉后面那一串首字母小写就是属性名;
     *
     *      所有getter/setter都自动生成！
     */
```


---
## AOP介绍

AOP:(Aspect Oriented Programming)面向切面编程<br>
OOP:(Object Oriented Programming)面向对象编程

面向切面编程:基于OOP基础之上新的编程思想；<br>
指在程序运行期间,将某段代码`动态的切入`到指定方法的指定位置进行运行的这种编程方式,面向切面编程

### 动态代理添加日志
场景：计算器运行计算方法的时候进行日志记录；<br>
加日志记录：<br>
1）、直接编写在方法内部；不推荐，修改维护麻烦；

+ 日志记录：系统的辅助功能；
+ 业务逻辑：（核心功能）
+ 耦合；

2）、我们希望的是；
+ 业务逻辑：（核心功能）；日志模块；在核心功能运行期间，自己动态的加上；
+ 运行的时候，日志功能可以加上；

可以使用动态代理来将日志代码动态的在目标方法执行前后先进行执行；

```java
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.util.Arrays;

import com.atguigu.inter.Calculator;
import com.atguigu.utils.LogUtils;

/**
 * 帮Calculator.java生成代理对象的类
 * Object newProxyInstance
 * (ClassLoader loader, Class<?>[] interfaces, InvocationHandler h)
 *
 * @author lfy
 *
 */
public class CalculatorProxy {

    /**
     * 为传入的参数对象创建一个动态代理对象
     * @param calculator
     * @return
     *
     * Calculator calculator:被代理对象；
     */
    public static Calculator getProxy(final Calculator calculator) {
        // TODO Auto-generated method stub

        //方法执行器。帮我们目标对象执行目标方法
        InvocationHandler h = new InvocationHandler() {
            /**
             * Object proxy：代理对象；给jdk使用，任何时候都不要动这个对象
             * Method method：当前将要执行的目标对象的方法
             * Object[] args：这个方法调用时外界传入的参数值
             */
            @Override
            public Object invoke(Object proxy, Method method, Object[] args)
                    throws Throwable {
                
                //System.out.println("这是动态代理将要帮你执行方法...");
                Object result = null;
                try {
                    LogUtils.logStart(method, args);

                    // 利用反射执行目标方法
                    //目标方法执行后的返回值
                    result = method.invoke(calculator, args);
                    LogUtils.logReturn(method, result);
                } catch (Exception e) {
                    LogUtils.logException(method,e);
                }finally{
                    LogUtils.logEnd(method);

                }

                //返回值必须返回出去外界才能拿到真正执行后的返回值
                return result;
            }
        };
        Class<?>[] interfaces = calculator.getClass().getInterfaces();
        ClassLoader loader = calculator.getClass().getClassLoader();

        //Proxy为目标对象创建代理对象；
        Object proxy = Proxy.newProxyInstance(loader, interfaces, h);
        return (Calculator) proxy;
    }

}
```

动态代理：
1. 写起来难；
2. **jdk默认的动态代理，如果目标对象没有实现任何接口，是无法为他创建代理对象的;**

Spring动态代理难；Spring实现了AOP功能；底层就是动态代理；
+ 可以利用Spring一句代码都不写的去创建动态代理；实现简单，而且没有强制要求目标对象必须实现接口；

`将某段代码（日志）` **动态的切入（不把日志代码写死在业务逻辑方法中）** 到`指定方法（加减乘除）`的`指定位置（方法的开始、结束、异常。。。）`进行运行的这种编程方式（Spring简化了面向切面编程）

AOP专业术语

![无法加载图片](https://huteng-dev.github.io/img/aop-word.png)

### AOP使用步骤：

1.导包；

+ Spring基础的包：
    + commons-logging-1.1.3.jar
    + spring-aop-4.0.0.RELEASE.jar
    + spring-beans-4.0.0.RELEASE.jar
    + spring-context-4.0.0.RELEASE.jar
    + spring-core-4.0.0.RELEASE.jar
    + spring-expression-4.0.0.RELEASE.jar

+ Spring支持面向切面编程的包是：
    + spring-aspects-4.0.0.RELEASE.jar：基础版

+ 加强版的面向切面编程（即使目标对象没有实现任何接口也能创建动态代理）
    + com.springsource.net.sf.cglib-2.2.0.jar
    + com.springsource.org.aopalliance-1.0.0.jar
    + com.springsource.org.aspectj.weaver-1.6.8.RELEASE.jar

2.写配置；

1. 将目标类和切面类（封装了通知方法（在目标方法执行前后执行的方法））加入到ioc容器中
2. 还应该告诉Spring到底哪个是切面类`@Aspect`
3. 告诉Spring，切面类里面的每一个方法，都是何时何地运行；

```java
/**
*5个通知注解
*   @Before:在目标方法之前运行;                 前置通知
*   @After: 在目标方法结束之后;                 后置通知
*   @AfterReturning:在目标方法正常返回之后;     返回通知
*   @AfterThrowing:在目标方法抛出异常之后运行;  异常通知
*   @Around:环绕;                             环绕通知
*/

//切入点表达式
//execution(访问权限 返回值类型 方法签名)
@Before("execution(public int com.atguigu.impl.MyMathCalculator.*(int, int))")
    public static void logStart(){
        System.out.println("【xxx】方法开始执行，用的参数列表【xxx】");
    }

    //想在目标方法正常执行完成之后执行
    @AfterReturning("execution(public int com.atguigu.impl.MyMathCalculator.*(int, int))")
    public static void logReturn(){
        System.out.println("【xxxx】方法正常执行完成，计算结果是：");
    }

    //想在目标方法出现异常的时候执行
    @AfterThrowing("execution(public int com.atguigu.impl.MyMathCalculator.*(int, int))")
    public static void logException() {
        System.out.println("【xxxx】方法执行出现异常了，异常信息是：；这个异常已经通知测试小组进行排查");
    }

    //想在目标方法结束的时候执行
    @After("execution(public int com.atguigu.impl.MyMathCalculator.*(int, int))")
    public static void logEnd() {
        System.out.println("【xxx】方法最终结束了");
    }
```

3.开启基于注解的AOP模式

在配置文件中开启基于注解的AOP功能；AOP名称空间

```xml
<aop:aspectj-autoproxy></aop:aspectj-autoproxy>
```
4.测试；

```java
Calculator bean = ioc.getBean(Calculator.class);
bean.add(2, 1);
```

### AOP切入点表达式细节

```java
/**
	 * 切入点表达式的写法；
	 * 固定格式： execution(访问权限符  返回值类型  方法全类名(参数表))
	 *   
	 * 通配符：
	 * 		*：
	 * 			1）匹配一个或者多个字符:execution(public int com.atguigu.impl.MyMath*r.*(int, int))
	 * 			2）匹配任意一个参数：第一个是int类型，第二个参数任意类型；（匹配两个参数）
	 * 				execution(public int com.atguigu.impl.MyMath*.*(int, *))
	 * 			3）只能匹配一层路径
	 * 			4）权限位置*不能；权限位置不写就行；public【可选的】
	 * 		..：
	 * 			1）匹配任意多个参数，任意类型参数
	 * 			2）匹配任意多层路径:
	 * 				execution(public int com.atguigu..MyMath*.*(..));
	 * 
	 * 记住两种；
	 * 最精确的：execution(public int com.atguigu.impl.MyMathCalculator.add(int,int))
	 * 最模糊的：execution(* *.*(..))：千万别写；
	 * 
	 * &&”、“||”、“!
	 * 
	 * &&：我们要切入的位置满足这两个表达式
	 * 	MyMathCalculator.add(int,double)
	 * execution(public int com.atguigu..MyMath*.*(..))&&execution(* *.*(int,int))
	 * 
	 * 
	 * ||:满足任意一个表达式即可
	 * execution(public int com.atguigu..MyMath*.*(..))||execution(* *.*(int,int))
	 * 
	 * !：只要不是这个位置都切入
	 * !execution(public int com.atguigu..MyMath*.*(..))
	 * 

	 */
```

### 拿到目标方法的详细信息



+ 只需要为通知方法的参数列表上写一个参数：JoinPoint joinPoint(org.aspectj.lang包)：封装了当前目标方法的详细信息

```java
@Before("execution(public int com.atguigu.impl.MyMathCalculator.*(..))")
	public static void logStart(JoinPoint joinPoint){
		//获取到目标方法运行是使用的参数
		Object[] args = joinPoint.getArgs();
		//获取到方法签名
		Signature signature = joinPoint.getSignature();
		String name = signature.getName();
		System.out.println("【"+name+"】方法开始执行，用的参数列表【"+Arrays.asList(args)+"】");
	}
```

+ 告诉Spring哪个参数是用来接收异常throwing="exception"：告诉Spring哪个参数是用来接收异常;告诉Spring这个result用来接收返回值：returning="result"；(用法相同)

```java
@AfterThrowing(value="execution(public int com.atguigu.impl.MyMathCalculator.*(..))",throwing="exception")
	public static void logException(JoinPoint joinPoint,Exception exception) {
		System.out.println("【"+joinPoint.getSignature().getName()+"】方法执行出现异常了，异常信息是【"+exception+"】：；这个异常已经通知测试小组进行排查");
	}
```

+ Exception exception:指定通知方法可以接收哪些异常

**方法的参数列表一定不能乱写**

### 环绕通知

```java
/**
	 * @Around：环绕	:是Spring中强大的通知；
	 * @Around：环绕:动态代理；
	 * 	try{
	 * 			//前置通知
	 * 			method.invoke(obj,args);
	 * 			//返回通知
	 * 	}catch(e){
	 * 			//异常通知
	 *  }finally{
	 * 			//后置通知
	 * 	}
	 * 		
	 * 	四合一通知就是环绕通知；
	 * 	环绕通知中有一个参数：	ProceedingJoinPoint 
	 * 
	 *环绕通知：是优先于普通通知执行，执行顺序；
	 *
	 *[普通前置]
	 *{
	 *	try{
	 *		环绕前置
	 *		环绕执行：目标方法执行
	 *		环绕返回
	 *	}catch(){
	 *		环绕出现异常
	 *	}finally{
	 *		环绕后置
	 *	}
	 *}
	 *
	 *
	 *[普通后置]
	 *[普通方法返回/方法异常]
	 *新的顺序：
	 *		（环绕前置---普通前置）----目标方法执行----环绕正常返回/出现异常-----环绕后置----普通后置---普通返回或者异常
    *
    *如果有对同一个目标方法有两个切面的话，按首字母的顺序执行（或使用@Order(int)来改变顺序【数值越小优先级越高】）；
    *执行顺序类似于一条线贯穿同心圆，先执行前置的，后置最后执行
	 */
```
 
### 基于配置的AOP使用方法

```xml
	<!--  开启基于注解的AOP功能；aop名称空间-->
	
	<!--  基于配置的AOP-->
	<bean id="myMathCalculator" class="com.atguigu.impl.MyMathCalculator"></bean>
	<bean id="BValidateApsect" class="com.atguigu.utils.BValidateApsect"></bean>
	<bean id="logUtils" class="com.atguigu.utils.LogUtils"></bean>
	
	<!-- 需要AOP名称空间 -->
	<aop:config>
		<aop:pointcut expression="execution(* com.atguigu.impl.*.*(..))" id="globalPoint"/>
        <!-- 方便调用 -->
	
		<!-- 普通前置  ===== 目标方法  =====(环绕执行后置/返回)====普通后置====普通返回    -->
		<!-- 指定切面：@Aspect -->
		<aop:aspect ref="logUtils" order="1">
			<!-- 配置哪个方法是前置通知；method指定方法名 
			logStart@Before("切入点表达式")
			-->
			<!-- 当前切面能用的 -->
			<aop:around method="myAround" pointcut-ref="mypoint"/>
			<aop:pointcut expression="execution(* com.atguigu.impl.*.*(..))" id="mypoint"/>
			<aop:before method="logStart" pointcut="execution(* com.atguigu.impl.*.*(..))"/>
			<aop:after-returning method="logReturn" pointcut-ref="mypoint" returning="result"/>
			<aop:after-throwing method="logException" pointcut-ref="mypoint" throwing="exception"/>
			<aop:after method="logEnd" pointcut-ref="mypoint"/>
		</aop:aspect>
	
		<aop:aspect ref="BValidateApsect" order="3">
			<aop:before method="logStart" pointcut-ref="globalPoint"/>
			<aop:after-returning method="logReturn" pointcut-ref="globalPoint" returning="result"/>
			<aop:after-throwing method="logException" pointcut-ref="globalPoint" throwing="exception"/>
			<aop:after method="logEnd" pointcut-ref="globalPoint"/>
		</aop:aspect>
		<!-- 在切面类中使用五个通知注解来配置切面中的这些通知方法都何时何地运行 -->
	</aop:config>
```

### AOP使用场景

+ AOP加日志保存到数据库；
+ AOP做权限验证；
+ AOP做安全检查；
+ AOP做事务控制


---
此文档为在B站学习ssm框架的笔记以及从其他地方整理的资料（[点击访问原视频](https://www.bilibili.com/video/BV1d4411g7tv?p=1 "尚硅谷雷丰阳大神的Spring、Spring MVC、MyBatis课程")）
