From ubuntu:16.04

MAINTAINER Louie Long <longyu805@163.com>
LABEL version="0.1" description="web vedio server Container"

# 使用清华源
#COPY docker/sources.list /etc/apt/sources.list

# 使用网易源
RUN  sed -i s@/archive.ubuntu.com/@/mirrors.163.com/@g /etc/apt/sources.list

# 使用ubuntu安装必要的软件
RUN \
    apt-get update \
&& \
    apt-get install -y \
            vim \
            git \
            nginx \
            python \
            python-pip \
            python-setuptools \
            --no-install-recommends \
&& \
    apt-get update

# 使用pip安装必须要的软件
RUN \
    pip install --upgrade pip \
&& \
    pip install tornado

# 添加ares代码
ADD ares /home/ares/

# 拷贝ngnix配置文件
COPY docker/nginx.conf /etc/nginx/nginx.conf

# 启动nginx服务器
CMD /usr/sbin/nginx

# 指定工作目录
WORKDIR /home/ares

# 指定家目录文件
ENV HOME /home/ares

# 中文支持 
ENV LANG C.UTF-8

# 映射容器端口
EXPOSE 8000

#RUN python /home/ares/web_video_server.py &
ENTRYPOINT cd /home/ares && python web_video_server.py 
#ENTRYPOINT /bin/bash 
