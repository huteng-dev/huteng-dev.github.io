---
    layout: post
    title: "Docker学习(1)"
    date: 2021-07-09 09:20:15
    categories: docker 笔记
---

Docker 是一个开源的应用容器引擎，基于 Go 语言 并遵从 Apache2.0 协议开源。Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。


* 目录
{:toc}

# 介绍

## 优点

1. 更高效的利用系统资源
2. 更快速的启动时间
3. 一致的运行环境
4. 持续交付和部署
> 使用 Docker 可以通过定制应用镜像来实现持续集成、持续交付、部署。开发人员可以通过 Dockerfile 来进行镜像构建，并结合 持续集成(Continuous Integration) 系统进行集成测试，而运维人员则可以直接在生产环境中快速部署该镜像，甚至结合 持续部署(Continuous Delivery/Deployment) 系统进行自动部署。
5. 更轻松的迁移
6. 更轻松的维护和扩展

## 与传统虚拟机区别

特性|容器|虚拟机
--|--|--
启动|秒级|分钟级
硬盘使用|一般为 MB|一般为 GB
性能|接近原生|弱于
系统支持量|单机支持上千个容器|一般几十个

## Docker架构

![这里是张图片](https://huteng-dev.github.io/img/docker-on-linux.png "Docker架构图片")

## Docker 包括三个基本概念

+ 镜像（Image）
+ 容器（Container）
+ 仓库（Repository）

### 镜像

操作系统分为**内核**和**用户空间**。对于 Linux 而言，内核启动后，会挂载**root**文件系统为其提供用户空间支持。而 Docker 镜像（Image），就相当于是一个 root 文件系统。比如官方镜像 ubuntu:18.04 就包含了完整的一套 Ubuntu 18.04 最小系统的 root 文件系统。

Docker 镜像 是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。镜像 不包含 任何动态数据，其内容在构建之后也不会被改变。

### 容器

镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的 类 和 实例 一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。

容器的实质是进程，但与直接在宿主执行的进程不同，容器进程运行于属于自己的独立的 命名空间。因此容器可以拥有自己的 root 文件系统、自己的网络配置、自己的进程空间，甚至自己的用户 ID 空间。容器内的进程是运行在一个隔离的环境里，使用起来，就好像是在一个独立于宿主的系统下操作一样。这种特性使得容器封装的应用比直接在宿主运行更加安全。

### 仓库

镜像构建完成后，可以很容易的在当前宿主机上运行，但是，如果需要在其它服务器上使用这个镜像，我们就需要一个集中的存储、分发镜像的服务，__Docker Registry__ 就是这样的服务。
通常一个 Docker Registry 中可以包含多个 仓库（Repository）；每个仓库可以包含多个 标签（Tag）；每个标签对应一个镜像。
通常，一个仓库会包含同一个软件不同版本的镜像，而标签就常用于对应该软件的各个版本。我们可以通过 <仓库名>:<标签> 的格式来指定具体是这个软件哪个版本的镜像。如果不给出标签，将以 latest 作为默认标签。

# 安装(CentOS)

Docker 分为 stable test 和 nightly 三个更新频道。

## 配置YUM源并安装

``` sh
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo 
#阿里的docker镜像源

# 官方源
# $ sudo yum-config-manager \
#     --add-repo \
#     https://download.docker.com/linux/centos/docker-ce.repo

yum list docker-ce --showduplicates | sort -r
#查看仓库中所有docker版本
#版本列表中的版本号为第二列，版本列表第一行第二列中的 3:19.03.8-3.e17 表示版本为 19.03.8 ，19.03.8才是实际要指定的版本号。

sudo yum install -y docker-ce
#安装最新版本

sudo yum install -y docker-ce-19.03.6
#安装指定版本,19.03.6版本

curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh --mirror Aliyun
#使用脚本自动安装
```

__CentOS8 额外设置__

由于 CentOS8 防火墙使用了 nftables，但 Docker 尚未支持 nftables
```sh
vi /etc/firewalld/firewalld.conf

FirewallBackend=iptables
# FirewallBackend=nftables
#更改

firewall-cmd --permanent --zone=trusted --add-interface=docker0
firewall-cmd --reload
#或者执行上述命令
```

## 启动
```sh
sudo systemctl enable docker
sudo systemctl start docker
#启动

sudo groupadd docker
#建立用户组

sudo usermod -aG docker $USER
#将当前用户加入docker组
```
__添加内核参数__

如果在 CentOS 使用 Docker 看到下面的这些警告信息：
```sh
WARNING: bridge-nf-call-iptables is disabled
WARNING: bridge-nf-call-ip6tables is disabled
```
添加内核配置参数以启用这些功能
```sh
$ sudo tee -a /etc/sysctl.conf <<-EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

sudo sysctl -p
#重新加载 sysctl.conf
```

## 验证
```sh
$ docker
Usage:  docker COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/root/.docker")
  -D, --debug              Enable debug mode
      --help               Print usage
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/root/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/root/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/root/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit
```

## 镜像加速

国内从 Docker Hub 拉取镜像有时会遇到困难，此时可以配置镜像加速器。国内很多云服务商都提供了国内加速器服务，例如：

+ 阿里云加速器(点击管理控制台 -> 登录账号(淘宝账号) -> 右侧镜像工具 -> 镜像加速器 -> 复制加速器地址)
+ 网易云加速器 https://hub-mirror.c.163.com
+ 百度云加速器 https://mirror.baidubce.com

Ubuntu 16.04+、Debian 8+、CentOS 7+
目前主流 Linux 发行版均已使用 systemd 进行服务管理，这里介绍如何在使用 systemd 的 Linux 发行版中配置镜像加速器。
请首先执行以下命令，查看是否在 docker.service 文件中配置过镜像地址。
```sh
$ systemctl cat docker | grep '\-\-registry\-mirror'
```
如果该命令有输出，那么请执行
```sh
 $ systemctl cat docker
 ```
  查看 ExecStart= 出现的位置，修改对应的文件内容去掉 --registry-mirror 参数及其值，并按接下来的步骤进行配置。
如果以上命令没有任何输出，那么就可以在 /etc/docker/daemon.json 中写入如下内容（如果文件不存在请新建该文件）：
```json
{
  "registry-mirrors": [
    "https://hub-mirror.c.163.com",
    "https://mirror.baidubce.com"
  ]
}
```
注意，一定要保证该文件符合 json 规范，否则 Docker 将不能启动。
之后重新启动服务。
```sh
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```

## 使用镜像

从 Docker 镜像仓库获取镜像的命令是 docker pull。其命令格式为：
```sh
$ docker pull [选项] [Docker Registry 地址[:端口号]/]仓库名[:标签]
```

+ Docker 镜像仓库地址：地址的格式一般是 <域名/IP>[:端口号]。默认地址是 Docker Hub(docker.io)。
+ 仓库名：如之前所说，这里的仓库名是两段式名称，即 <用户名>/<软件名>。对于 Docker Hub，如果不给出用户名，则默认为 library，也就是官方镜像。
```sh
#启动docker
systemctl start docker

#停止docker
systemctl stop docker

#重启docker
systemctl restart docker

#查看docker状态
systemctl status docker

#设置开机启动
systemctl enable docker

#查看docker概要信息
docker info
```