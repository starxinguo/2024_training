# Linux学习
这里由于是基于vmware虚拟机安装的ubuntu系统来进行操作实现的，且平常在校的课程学习涉及到相关内容，因此主要记录在平常的操作中会使用到的一些相关指令，会根据额外的学习，来补充相关的指令。
## 1.1 文件指令
ls: 列出当前目录下的文件和子目录。可以使用 -l 参数查看详细信息。  

cd: 切换到指定目录。cd .. 可以返回上一级目录。  

mkdir: 创建新的目录。mkdir my_dir 会创建一个名为 my_dir 的新目录。  

touch: 创建新的文件。touch my_file.txt 会创建一个名为 my_file.txt 的新文件。  

rm: 删除文件或目录。rm my_file.txt 会删除 my_file.txt 文件。

rm -r my_dir 会递归删除 my_dir 目录及其下的所有内容。  

cp: 复制文件或目录。cp my_file.txt my_copy.txt 会创建 my_copy.txt 作为 my_file.txt 的副本。  

mv: 移动或重命名文件或目录。mv my_file.txt new_name.txt 会将 my_file.txt 重命名为 new_name.txt。  

## 1.2 磁盘操作
df: 查看文件系统的磁盘使用情况。  
df -h 会以人类可读的格式显示磁盘使用情况。

du: 查看指定目录或文件的磁盘占用情况。  
du -h my_dir 会显示 my_dir 目录及其子目录的磁盘使用情况。

fdisk: 管理磁盘分区。  
fdisk /dev/sda 可以对 /dev/sda 磁盘进行分区操作。

mkfs: 在磁盘分区上创建文件系统。  
mkfs.ext4 /dev/sda1 会在 /dev/sda1 分区上创建 ext4 文件系统。

mount: 挂载文件系统。  
mount /dev/sda1 /mnt 会将 /dev/sda1 分区挂载到 /mnt 目录下。  
umount: 卸载文件系统。umount /mnt 会卸载 /mnt 目录下挂载的文件系统。

## 1.3 其他常用命令
会随着学习操作时，不断补充可以用到的命令。

cat: 查看文件内容。  
cat my_file.txt 会显示 my_file.txt 的全部内容。  

grep: 在文件中搜索匹配的字符串。  
grep "keyword" my_file.txt 会在 my_file.txt 中搜索包含 "keyword" 的行。

find: 在目录中搜索文件。  
find . -name "*.txt" 会在当前目录及其子目录中搜索所有 .txt 文件。

tar: 创建和操作压缩文件。  
tar -czf my_archive.tar.gz my_dir 会创建一个名为 my_archive.tar.gz 的压缩包,包含 my_dir 目录及其子目录。

sudo:特级操作指令。
sudo -s:进入特级操作。