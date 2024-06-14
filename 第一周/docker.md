# docker学习
这里主要讲解docker的安装与docker-compose的安装，以及在实践过程中，需要用到的docker指令，关于mysql与redis容器的操作，放到mysql.md与redis.md文件中进行讲解。
## 1.1 docker安装
编辑/etc/apt/source.list  

修改镜像源(阿里云/华为/清华园)
可以参考此博客更新系统源：
https://blog.csdn.net/weixin_43532644/article/details/108225437?ops_request_misc=%7B

>sudo apt-get update
更新 Ubuntu 系统中可用软件包的索引列表。

>sudo apt-get upgrade

接下来安装docker。直接使用apt-get安装的docker为20.10版本，我们要使用的k8s并不支持这个版本，因此我安装19.03版本的docker，以规避因版本出现的一些问题。  

### 安装必要的工具
>sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common

### 添加 Docker 官方 GPG 密钥
>curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

### 添加 Docker CE 的稳定版软件源
>sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

### 更新 APT 软件包缓存
>sudo apt-get update

### 安装 Docker CE 19.03 版本
>sudo apt-get install -y docker-ce=5:19.03.*~3-0~ubuntu-$(lsb_release -cs) docker-ce-cli=5:19.03.*~3-0~ubuntu-$(lsb_release -cs) containerd.io

>sudo systemctl enable docker  
>sudo systemctl daemon-reload  
>sudo systemctl restart docker  

## 1.2安装docker-compose

### 基于github安装
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

给下载的文件加执行权限  
chmod +x /usr/local/bin/docker-compose  

### 检查是否安装成功
docker-compose version

## 1.3 docker相关指令
