---
    layout: post
    title: "Lambda学习"
    date: 2021-09-14 16:07:24
    categories: JDK1.8 lambda 匿名表达式
---

Java 8的一个大亮点是引入Lambda表达式，使用它设计的代码会更加简洁。当开发者在编写Lambda表达式时，也会随之被编译成一个函数式接口。通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。


* 目录
{:toc}


# 特性


> + 可选类型声明：不需要声明参数类型，编译器可以统一识别参数值。
> + 可选的参数圆括号：一个参数无需定义圆括号，但多个参数需要定义圆括号。
> + 可选的大括号：如果主体包含了一个语句，就不需要使用大括号。
> + 可选的返回关键字：如果主体只有一个表达式返回值则编译器会自动返回值，大括号需要指定表达式返回了一个数值。

# 例子
```java
// 1. 不需要参数,返回值为 5  
() -> 5  
  
// 2. 接收一个参数(数字类型),返回其2倍的值  
x -> 2 * x  
  
// 3. 接受2个参数(数字),并返回他们的差值  
(x, y) -> x – y  
  
// 4. 接收2个int型整数,返回他们的和  
(int x, int y) -> x + y  
  
// 5. 接受一个 string 对象,并在控制台打印,不返回任何值(看起来像是返回void)  
(String s) -> System.out.print(s)
```

除了Lambda表达式，可以直接传入方法引用。例如：

```java
public class Main {
    public static void main(String[] args) {
        String[] array = new String[] { "Apple", "Orange", "Banana", "Lemon" };
        Arrays.sort(array, Main::cmp);
        System.out.println(String.join(", ", array));
    }

    static int cmp(String s1, String s2) {
        return s1.compareTo(s2);
    }
}

```
Main::cmp   __::__是方法引用的标识符，表示引用main下的cmp方法(同理String::compareTo)；构造方法的引用写法是类名::new。


FunctionalInterface: __把只定义了单方法的接口称之为FunctionalInterface，用注解@FunctionalInterface标记。__

# Stream
Java从8开始，不但引入了Lambda表达式，还引入了一个全新的流式API：Stream API。它位于java.util.stream包中。

**这个Stream不同于java.io的InputStream和OutputStream，它代表的是任意Java对象的序列。**

-|java.io|	java.util.stream
--|--|--
存储|顺序读写的byte或char|顺序输出的任意Java对象实例
用途|序列化至文件或网络|内存计算／业务逻辑

**这个Stream和List也不一样**

-|java.util.List|java.util.stream
--|--|--
元素|已分配并存储在内存|可能未分配，实时计算
用途|操作一组已存在的Java对象|惰性计算



惰性计算的特点是：__一个Stream转换为另一个Stream时，实际上只存储了转换规则，并没有任何计算发生。__

```java
int result = createNaturalStream() // 创建Stream
             .filter(n -> n % 2 == 0) // 任意个转换
             .map(n -> n * n) // 任意个转换
             .limit(100) // 任意个转换
             .sum(); // 最终计算结果

```

Stream API的特点是：
+ Stream API提供了一套新的流式处理的抽象序列；
+ Stream API支持函数式编程和链式操作；
+ Stream可以表示无限序列，并且大多数情况下是惰性求值的。(它可以“存储”有限个或无限个元素。这里的存储打了个引号，是因为元素有可能已经全部存储在内存中，也有可能是根据需要实时计算出来的。)

## 创建

+ 直接用Stream.of()静态方法，传入可变参数即创建了一个能输出确定元素的Stream
```java
public class Main {
public static void main(String[] args) {
    Stream<String> stream = Stream.of("A", "B", "C", "D");
    // forEach()方法相当于内部循环调用，
    // 可传入符合Consumer接口的void accept(T t)的方法引用：
    stream.forEach(System.out::println);
}
}
```
+ 基于一个数组或者Collection，这样该Stream输出的元素就是数组或者Collection持有的元素
```java
public class Main {
    public static void main(String[] args) {
        Stream<String> stream1 = Arrays.stream(new String[] { "A", "B", "C" });
        Stream<String> stream2 = List.of("X", "Y", "Z").stream();
        stream1.forEach(System.out::println);
        stream2.forEach(System.out::println);
    }
}

```

+ 通过Stream.generate()方法，它需要传入一个Supplier对象
```java
public class Main {
    public static void main(String[] args) {
        Stream<Integer> natual = Stream.generate(new NatualSupplier());
        // 注意：无限序列必须先变成有限序列再打印:
        natual.limit(20).forEach(System.out::println);
    }
}

class NatualSupplier implements Supplier<Integer> {
    int n = 0;
    public Integer get() {
        n++;
        return n;
    }
}
```
> 对于无限序列，如果直接调用forEach()或者count()这些最终求值操作，会进入死循环，因为永远无法计算完这个序列，所以正确的方法是先把无限序列变成有限序列，例如，用limit()方法可以截取前面若干个元素，这样就变成了一个有限序列，对这个有限序列调用forEach()或者count()操作就没有问题。

+ 通过一些API提供的接口，直接获得Stream
```java
try (Stream<String> lines = Files.lines(Paths.get("/path/to/file.txt"))) {
    ...
}
```

因为Java的范型不支持基本类型，所以我们无法用Stream<int>这样的类型，会发生编译错误。为了保存int，只能使用Stream<Integer>，但这样会产生频繁的装箱、拆箱操作。为了提高效率，Java标准库提供了IntStream、LongStream和DoubleStream这三种使用基本类型的Stream，它们的使用方法和范型Stream没有大的区别，设计这三个Stream的目的是提高运行效率：
```java
// 将int[]数组变为IntStream:
IntStream is = Arrays.stream(new int[] { 1, 2, 3 });
// 将Stream<String>转换为LongStream:
LongStream ls = List.of("1", "2", "3").stream().mapToLong(Long::parseLong);
```

## 使用Map

Stream.map()是Stream最常用的一个转换方法，它把一个Stream转换为另一个Stream。所谓map操作，就是把一种操作运算，映射到一个序列的每一个元素上。例如，对x计算它的平方，可以使用函数f(x) = x * x。我们把这个函数映射到一个序列1，2，3，4，5上，就得到了另一个序列1，4，9，16，25

### map()

map()方法接收的对象是Function接口对象，它定义了一个apply()方法，负责把一个T类型转换成R类型
```java
@FunctionalInterface
public interface Function<T, R> {
    // 将T类型转换为R:
    R apply(T t);
}
```

map例子
```java
public class Main {
    public static void main(String[] args) {
        List.of("  Apple ", " pear ", " ORANGE", " BaNaNa ")
                .stream()
                .map(String::trim) // 去空格
                .map(String::toLowerCase) // 变小写
                .forEach(System.out::println); // 打印
    }
}
```

### filter()

Stream.filter()是Stream的另一个常用转换方法。

所谓filter()操作，就是对一个Stream的所有元素一一进行测试，不满足条件的就会被“滤掉”，剩下的满足条件的元素就构成了一个新的Stream。

filter()方法接收的对象是Predicate接口对象，它定义了一个test()方法，负责判断元素是否符合条件：
```java
@FunctionalInterface
public interface Predicate<T> {
    // 判断元素t是否符合条件:
    boolean test(T t);
}
```

例子
```java
public class Main {
    public static void main(String[] args) {
        IntStream.of(1, 2, 3, 4, 5, 6, 7, 8, 9)
                .filter(n -> n % 2 != 0)
                .forEach(System.out::println);
    }
}
```

map()和filter()都是Stream的转换方法，而Stream.reduce()则是Stream的一个聚合方法，它可以把一个Stream的所有元素按照聚合函数聚合成一个结果。

### reduce()

reduce()操作首先初始化结果为指定值（这里是0），紧接着，reduce()对每个元素依次调用(acc, n) -> acc + n，其中，acc是上次计算的结果：
```java
public class Main {
    public static void main(String[] args) {
        int s = Stream.of(1, 2, 3, 4, 5, 6, 7, 8, 9).reduce(0, (acc, n) -> acc + n);
        System.out.println(s); // 362880
    }
}
```

除了可以对数值进行累积计算外，灵活运用reduce()也可以对Java对象进行操作。
```java
public class Main {
    public static void main(String[] args) {
        // 按行读取配置文件:
        List<String> props = List.of("profile=native", "debug=true", "logging=warn", "interval=500");
        Map<String, String> map = props.stream()
                // 把k=v转换为Map[k]=v:
                .map(kv -> {
                    String[] ss = kv.split("\\=", 2);
                    return Map.of(ss[0], ss[1]);
                })
                // 把所有Map聚合到一个Map:
                .reduce(new HashMap<String, String>(), (m, kv) -> {
                    m.putAll(kv);
                    return m;
                });
        // 打印结果:
        map.forEach((k, v) -> {
            System.out.println(k + " = " + v);
        });
    }
}
```

### collect()

把Stream的每个元素收集到List的方法是调用collect()并传入Collectors.toList()对象，它实际上是一个Collector实例，通过类似reduce()的操作，把每个元素添加到一个收集器中（实际上是ArrayList）。

类似的，collect(Collectors.toSet())可以把Stream的每个元素收集到Set中。


Stream还有一个强大的分组功能，可以按组输出。
```java
public class Main {
    public static void main(String[] args) {
        List<String> list = List.of("Apple", "Banana", "Blackberry", "Coconut", "Avocado", "Cherry", "Apricots");
        Map<String, List<String>> groups = list.stream()
                .collect(Collectors.groupingBy(s -> s.substring(0, 1), Collectors.toList()));
        System.out.println(groups);
    }
}
```
分组输出使用Collectors.groupingBy()，它需要提供两个函数：一个是分组的key，这里使用s -> s.substring(0, 1)，表示只要首字母相同的String分到一组，第二个是分组的value，这里直接使用Collectors.toList()，表示输出为List.

## 其他操作

### 排序

对Stream的元素进行排序十分简单，只需调用sorted()方法，此方法要求Stream的每个元素必须实现Comparable接口。如果要自定义排序，传入指定的Comparator即可
```java
List<String> list = List.of("Orange", "apple", "Banana")
    .stream()
    .sorted(String::compareToIgnoreCase)
    .collect(Collectors.toList());
```

### 去重

对一个Stream的元素进行去重，没必要先转换为Set，可以直接用distinct()
```java
List.of("A", "B", "A", "C", "B", "D")
    .stream()
    .distinct()
    .collect(Collectors.toList()); // [A, B, C, D]
```

### 截取

截取操作常用于把一个无限的Stream转换成有限的Stream，skip()用于跳过当前Stream的前N个元素，limit()用于截取当前Stream最多前N个元素
```java
List.of("A", "B", "C", "D", "E", "F")
    .stream()
    .skip(2) // 跳过A, B
    .limit(3) // 截取C, D, E
    .collect(Collectors.toList()); // [C, D, E]
```

### 合并

将两个Stream合并为一个Stream可以使用Stream的静态方法concat()
```java
Stream<String> s1 = List.of("A", "B", "C").stream();
Stream<String> s2 = List.of("D", "E").stream();
// 合并:
Stream<String> s = Stream.concat(s1, s2);
System.out.println(s.collect(Collectors.toList())); // [A, B, C, D, E]
```

### flatMap

如果Stream的元素是集合
```java
Stream<List<Integer>> s = Stream.of(
        Arrays.asList(1, 2, 3),
        Arrays.asList(4, 5, 6),
        Arrays.asList(7, 8, 9));

Stream<Integer> i = s.flatMap(list -> list.stream());
```

所谓flatMap()，是指把Stream的每个元素（这里是List）映射为Stream，然后合并成一个新的Stream.

### 并行

通常情况下，对Stream的元素进行处理是单线程的，即一个一个元素进行处理。但是很多时候，我们希望可以并行处理Stream的元素，因为在元素数量非常大的情况，并行处理可以大大加快处理速度。

把一个普通Stream转换为可以并行处理的Stream非常简单，只需要用parallel()进行转换
```java
Stream<String> s = ...
String[] result = s.parallel() // 变成一个可以并行处理的Stream
                   .sorted() // 可以进行并行排序
                   .toArray(String[]::new);
```
经过parallel()转换后的Stream只要可能，就会对后续操作进行并行处理。我们不需要编写任何多线程代码就可以享受到并行处理带来的执行效率的提升

## 其他聚合方法

+ 除了reduce()和collect()外，Stream还有一些常用的聚合方法：
  + count()：用于返回元素个数；
  + max(Comparator<? super T> cp)：找出最大元素；
  + min(Comparator<? super T> cp)：找出最小元素。

+ 针对IntStream、LongStream和DoubleStream，还额外提供了以下聚合方法：
  + sum()：对所有元素求和；
  + average()：对所有元素求平均数。

+ 还有一些方法，用来测试Stream的元素是否满足以下条件：
    + boolean allMatch(Predicate<? super T>)：测试是否所有元素均满足测试条件；
    + boolean anyMatch(Predicate<? super T>)：测试是否至少有一个元素满足测试条件。
+ 最后一个常用的方法是forEach()，它可以循环处理Stream的每个元素，我们经常传入System.out::println来打印Stream的元素


    