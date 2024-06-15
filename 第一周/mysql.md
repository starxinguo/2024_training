# mysql学习
主要讲解如何编写docker-compose.yml，从而利用docker-compose进行mysql的安装，同时记录一些mysql相关的指令。实验过程通过截图放在了*第一周/实验截图*里
## 1.1 mysql安装
这里实验的要求是通过docker-compose进行安装  
### docker-compose.yml编写  
>version: '3'  
services:  
    mysql:  
        environment:  
            MYSQL_ROOT_PASSWORD: "123456"  
        image: "mysql:latest"  
        container_name: mysql  
        restart: always  
        ##映射挂载  
        volumes:  
            - "/etc/docker/mysql:/var/lib/mysql"  
            - "./mysql:/docker-entrypoint-initdb.d/"  
        ports:  
            - "3306:3306"  

version: '3': 指定使用 Docker Compose 版本 3 的格式。  

services: 定义了一个名为 mysql 的服务。  

environment: 设置了 MySQL 容器的环境变量,其中MYSQL_ROOT_PASSWORD 是 MySQL 的 root 用户密码。  

image: "mysql:latest": 指定使用 Docker Hub 上的 MySQL 最新版本镜像。  

container_name: mysql: 定义了容器的名称为 mysql。  

restart: always: 设置容器在任何情况下都会自动重启。  

volumes:"/data/mysql:/var/lib/mysql": 将主机的 /data/mysql 目录挂载到容器的 /var/lib/mysql 目录,用于存储 MySQL 数据文件，这样可以保证数据的持久化。

"./mysql:/docker-entrypoint-initdb.d/": 将当前目录下的 mysql 目录挂载到容器的 /docker-entrypoint-initdb.d/ 目录,用于存放初始化 SQL 脚本。  

ports: 将容器的 3306 端口映射到宿主机的 3306 端口,用于外部访问 MySQL 服务。

## 1.2 mysql语句  
### 创建数据库
我们可以在登陆 MySQL 服务后，使用 create 命令创建数据库
>mysql -u root -p   
Enter password:******  # 登录后进入终端  
create DATABASE 数据库名;

创建数据库基本语法：
>CREATE DATABASE [IF NOT EXISTS] database_name  
  [CHARACTER SET charset_name]  
  [COLLATE collation_name];  

### 使用数据库
在 MySQL 中，要选择要使用的数据库，可以使用 USE 语句，以下是基本的语法：
>USE database_name;

选择好数据库后，后续的 SQL 查询和操作在指定的数据库 database_name 上执行。

### MySQL 数据类型
MySQL 支持所有标准 SQL 数值数据类型。

这些类型包括严格数值数据类型(INTEGER、SMALLINT、DECIMAL 和 NUMERIC)，以及近似数值数据类型(FLOAT、REAL 和 DOUBLE PRECISION)。

关键字INT是INTEGER的同义词，关键字DEC是DECIMAL的同义词。

### Mysql 创建数据表  
创建 MySQL 数据表需要以下信息：  
表名  
表字段名  
定义每个表字段的数据类型  
通用语法：
>CREATE TABLE table_name (  
    column1 datatype,  
    column2 datatype,  
    ...  
);

在创建表的时候，可以用一些关键字进行修饰，如 AUTO_INCREMENT 关键字用于创建一个自增长的列，PRIMARY KEY 用于定义主键。

### MySQL 插入数据
向MySQL数据表插入数据通用的 INSERT INTO SQL语法：
>INSERT INTO table_name (column1, column2, column3, ...)  
VALUES (value1, value2, value3, ...);

如果数据是字符型，必须使用单引号 ' 或者双引号 "，如： 'value1', "value1"。

### MySQL 查询语句
MySQL 数据库使用 SELECT 语句来查询数据。
>SELECT column1, column2, ...  
FROM table_name  
[WHERE condition]  
[ORDER BY column_name [ASC | DESC]]  
[LIMIT number];

WHERE condition 是一个可选的子句，用于指定过滤条件，只返回符合条件的行。  
ORDER BY column_name [ASC | DESC] 是一个可选的子句，用于指定结果集的排序顺序，默认是升序（ASC）。  
LIMIT number 是一个可选的子句，用于限制返回的行数。  

### MySQL 更新语句
如果我们需要修改或更新 MySQL 中的数据，我们可以使用 UPDATE 命令来操作。
>UPDATE table_name  
SET column1 = value1, column2 = value2, ...  
WHERE condition;
