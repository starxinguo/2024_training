# 第三周学习
主要讲解如何编写docker-compose.yml，从而利用docker-compose进行mysql的安装，同时记录一些mysql相关的指令。实验过程通过截图放在了*第一周/实验截图*里
## 1 mysql增删改查
这里实验的要求是通过docker-compose进行安装  
### 连接到mysql
由于我是通过PyMySQL 模块直接连接 MySQL 数据库，由该MySQL是创建于虚拟机里的docker容器，因此在连接时，需要设置好对于的ip地址，映射端口与mysql登录密码与用户名。  
>    db = pymysql.connect(  
        host='192.168.239.138',  
        user='root',  
        password='123456',  
        port=3306  
    )
### mysql增删改查
>cursor = db.cursor()  

创建一个游标对象,用于执行 SQL 查询并获取结果。  
而后编写好需要执行的sql命令，通过代码：
>cursor.execute()

执行对于的sql命令，即可实现mysql的增删改查。

### 实验学习与收获
* 在最开始连接mysql时，由于模块的缺少，导致一直无法连接到mysql，后续通过try...except,捕获相应的错误:  
error connecting to the database: 'cryptography' package is required for sha256_password or caching_sha2_password auth methods  
发现是因为mysql需要通过该模块进行身份验证，而python恰好未下载该模块，因此导致mysql无法连接，而后下载好该模块，即完成实验。

## 2 多线程下载任务