---
    layout: post
    title: "Docker学习(1)"
    date: 2021-07-09 09:20:15
    categories: docker 笔记
---

+ Docker 是一个开源的应用容器引擎，基于 Go 语言 并遵从 Apache2.0 协议开源。
+ Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。
+ 容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。

![这里是张图片](https://huteng-dev.github.io/img/docker-on-linux.png "Docker架构图片")


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

## Docker 包括三个基本概念
+ 镜像（Image）
+ 容器（Container）
+ 仓库（Repository）
### 镜像
