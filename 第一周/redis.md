# mysql学习
主要讲解如何编写docker-compose.yml，从而利用docker-compose进行redis的安装，同时记录一些mysql相关的指令。实验过程通过截图放在了*第一周/实验截图*里
## 1.1 mysql安装
这里实验的要求是通过docker-compose进行安装  
### docker-compose.yml编写  
>    redis:  
      image: "redis:latest"  
      container_name: redis  
      restart: always  
      command: redis-server --appendonly yes --requirepass  "123456"  
      ports:
        - "6379:6379"  
      volumes:  
        - "/etc/docker/redis:/data"

这段代码是一个 Docker 容器运行 Redis 服务的配置文件。让我们逐一分析一下各个部分的作用:

`image: "redis:latest"`:
   - 指定了要使用的 Redis 镜像,这里使用的是最新版本的 Redis 镜像。

`container_name: redis`:
   - 为这个 Redis 容器指定了名称为 "redis"。

`restart: always`:
   - 设置容器重启策略为 "always",即无论容器是何种原因退出,都会自动重启。

`command: redis-server --appendonly yes --requirepass "123456"`:
   - 在启动容器时,会执行 `redis-server` 命令,并传递两个参数:
     - `--appendonly yes`: 开启 AOF (Append-Only File) 持久化,将数据实时写入磁盘。
     - `--requirepass "123456"`: 设置 Redis 服务器的访问密码为 "123456"。

`ports:
     - "6379:6379"`:
   - 将容器内的 Redis 服务端口 6379 映射到宿主机的 6379 端口,这样外部就可以通过宿主机的 6379 端口访问 Redis 服务。

`volumes:
     - "/etc/docker/redis:/data"`:
   - 将容器内的 Redis 数据目录 `/data` 映射到宿主机的 `/etc/docker/redis` 目录,这样即使容器重启,数据也不会丢失。

总结起来,这段配置文件会启动一个 Redis 容器,将 Redis 服务端口映射到宿主机,设置了 Redis 的持久化和访问密码,并将容器内的数据目录映射到宿主机上,保证了数据的持久性。这样可以很方便地在 Docker 环境中部署和运行 Redis 服务。        

## 1.2 redis语句  
### 增加数据
使用 set 命令可以设置键值对:
>set key value
### 查询数据
使用 get 命令可以根据键获取值:
>get key
### 更新数据
使用 set 命令并指定已存在的键即可更新数据:
>set key new_value
### 删除数据
使用 del 命令可以删除指定的键值对:
>del key
### 列出所有键
使用 keys 命令可以列出所有的键:
>keys *
### 其他常用命令
设置键的过期时间(以秒为单位)
>expire key seconds  

查看键的剩余过期时间(以秒为单位)
>ttl key:

在列表左侧推入一个或多个值
>lpush key value1 [value2 ...]

设置哈希表中指定字段的值
>hset key field value