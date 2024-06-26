# 使用FLASK创建应用：个人主页
> <img style="width:200px; display: inline-block" src="img/dog-smile.png"/>

        发布个人主页，介绍个人履历

# 使用说明
## 1.创建并启动容器实例
```shell
cd flask_resume

# 构建
docker-compose build
[+] Building 0.3s (10/10) FINISHED                                                                       docker:default
 => [web internal] load build definition from Dockerfile                                                           0.0s
 => => transferring dockerfile: 256B                                                                               0.0s
 => [web internal] load metadata for docker.io/library/python:alpine                                               0.0s
 => [web internal] load .dockerignore                                                                              0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [web 1/5] FROM docker.io/library/python:alpine                                                                 0.0s
 => [web internal] load build context                                                                              0.0s
 => => transferring context: 65B                                                                                   0.0s
 => CACHED [web 2/5] WORKDIR /code                                                                                 0.0s
 => CACHED [web 3/5] COPY requirements.txt requirements.txt                                                        0.0s
 => CACHED [web 4/5] COPY pip.conf /etc/pip.conf                                                                   0.0s
 => CACHED [web 5/5] RUN pip install -r requirements.txt                                                           0.0s
 => [web] exporting to image                                                                                       0.0s
 => => exporting layers                                                                                            0.0s
 => => writing image sha256:eaf643ee1167b1f4c5d26328f6833284944dd9324129ff34c7d18057cc37c6c9                       0.0s
 => => naming to docker.io/library/resume:alpine                                                                   0.0s

# 创建并启动
docker-compose up -d
[+] Running 3/3
 ✔ Network python-br               Created                                                                         0.1s
 ✔ Container flask_resume-redis-1  Started                                                                         0.2s
 ✔ Container flask_resume-web-1    Started

# 构建成功会在主机生成镜像：resume:alpine
docker-compose images
CONTAINER              REPOSITORY          TAG                 IMAGE ID            SIZE
flask_resume-redis-1   redis               alpine              f597a450f464        40.7MB
flask_resume-web-1     resume              alpine              eaf643ee1167        69.4MB
```

## 2.域名地址映射配置
    Windows默认位置：C:\Windows\System32\drivers\etc\hosts
    Linux：/etc/hosts
    用文本编辑器以管理员模式打开hosts文件，在文件的结尾处增加一条记录，如下所示：
    
```ini
# 你也可以使用任何你喜欢的域名来替代 resume.dog
127.0.0.1 resume.dog www.resume.dog
```
    测试一下是否生效：
```shell
ping resume.dog
# 生效，输出如下：
正在 Ping hello.world [127.0.0.1] 具有 32 字节的数据:
来自 127.0.0.1 的回复: 字节=32 时间<1ms TTL=128
来自 127.0.0.1 的回复: 字节=32 时间<1ms TTL=128
来自 127.0.0.1 的回复: 字节=32 时间<1ms TTL=128
# 未生效
Ping 请求找不到主机 resume.dog。请检查该名称，换一个域名然后重试。
```

# 浏览器访问 http://resume.dog
> <img style="width:60%; display: inline-block" src="img/flask-resume-demo.png"/>
