# 简单的web视频服务器

A web application created by tornado web framework.

Use nginx to proxy tornado app.

## 1.视频服务器

**需求**：空闲机器存放视频资源，搭建一个web视频服务器可使局域网中其他pc或者手机、pad通过网页观看视频，从而节省硬盘空间。
**实现方法**：
本人web开发小白，在实现过程中首先了解到nginx本身可以处理mp4这种静态文件资源，通过编写html，然后浏览器直接打开html文件可以正常播放mp4视频，且可以拖拽进度条。但面临如何动态扫描特定目录并生成html页面的问题。由于之前听说过web框架（flask），而这些框架本身是python语言的，借助python语言可以实现扫描目录拿到文件列表，而这些web框架又支持模板渲染html页面，所以想到通过web框架实现。
先从flask开始，尝试了编写简单的web应用，最终结果可以完成播放任务，但发现拖拽进度条没有反应，有一定的功能缺陷。故改用tornado框架（主要是看到性能比较好，虽然项目可能没有那么高的性能需求，但还是用tornado了），编写完web框加后发现使用tornado的static_url能够处理静态资源，但处理方式总是先完全读取文件内容后再返回http响应，这样不仅导致硬盘处理有压力，也导致前端页面响应过慢，影响使用体验。
最终想到使用nginx反向代理tornado应用，tornado应用只返回html页面，而视频资源由nginx处理。最终实现web页面动态获取视频文件列表，点击后可以播放，而且支持拖拽进度条。
最终添加html5视频播放器videojs

Nginx反向代理tornado的配置请参考`ares/nginx.conf`
视频播放的端口为8000端口



## 2.docker镜像

为了更加方便的部署这套环境，将视频服务器环境打包进docker镜像，做到自动化部署，快速搭建。

### 2.1 配置文件

~~首先更换docker容器中的软件源为清华源，见文件`docker/sources.list`~~
Dockerfile中使用了163的源

然后更换docker容器中的nginx的配置，见文件`docker/nginx.conf`

端口映射：需要将docker容器中的8000端口映射个到宿主机的端口上，这里默认映射到8888端口

docker 容器构建 在docker目录之上使用使用命令 `docker build -t l0uie/ares:<tag> .`构建镜像

### 2.2 启动容器

使用如下命令启动ares容器。

```
sudo docker run --privileged=true -idt -p 8888:8000 -v /var/www/video/videos:/home/ares/videos  -v /var/run/docker.sock:/var/run/docker.sock  --name ares l0uie/ares:0.1.0
```

|   参数   |                    含义                    |      |
| :----: | :--------------------------------------: | ---- |
|   -p   |          映射宿主机的8888端口到容器的8000端口          |      |
|   -v   | 映射宿主机的目录到容器中，将本机的videos目录映射到容器中，以后只需将mp4格式的电影存放进宿主机的videos目录即可，可自行修改 |      |
| --name |              指定启动的容器名，可不使用               |      |
|   -d   |            后台运行，容器启动后自动在后台运行             |      |


