# git学习
由于本身的课程学习中涉及到相关的内容，因此在学习中我的重点在于内容的复习与实践。
## 1.1 git安装
直接通过官网选择符合自己电脑系统的git：[官网下载](https://git-scm.com/download)
## 1.2 git分支管理
*分支的创建和切换:*  
创建新分支: git branch (branch-name)  
切换到指定分支: git checkout (branch-name)  
创建并切换到新分支: git checkout -b (branch-name)  
  
*分支的合并:*  
合并分支: git merge (branch-name)   
合并时可能会发生冲突,需要手动解决冲突,根据平常实验时遇到的情况，当两个分支之间存在部分文件不相同时，可能会导致出现冲突。  
在 Git 中,merge 是一个非常重要的操作,它用于将一个分支合并到另一个分支上,从而合并两条独立的提交历史。通过 merge,我们可以将在不同分支上进行的开发工作整合到一起

*分支的查看和管理:*  
查看当前分支: git branch  
查看远程分支: git branch -r  
删除分支: git branch -d (branch-name)  

*分支策略（怎么样合理使用分支）:*   
主干分支(master/main): 用于保存稳定的版本  
开发分支(develop): 用于日常开发  
功能分支(feature): 用于开发新功能  
修复分支(hotfix): 用于修复生产环境的紧急 bug  

*分支的远程同步:*  
将本地分支推送到远程: git push origin （branch-name）  
拉取远程分支到本地: git pull origin （branch-name）  

*分支的重置和变基：*  
重置分支: git reset --hard （commit-id）  
变基分支: git rebase （branch-name）    

*关于rebase：*  
Rebase 是 Git 中一个非常强大但也较为复杂的功能,它可以用来整理、合并提交历史。与 merge 操作不同,rebase 会将当前分支的提交记录"重新应用"到指定的基底分支上,从而形成一条更加线性、整洁的提交历史。  
如果已经推送到远程仓库的提交记录被 rebase 了,就可能造成其他开发者的工作被覆盖。所以在公共分支上使用 rebase 时需要特别小心。

## 1.3 本地文件上传到github
具体指令如下：  
*git init*  
在当前目录下初始化一个新的 Git 仓库。
执行这条命令后,当前文件夹会被 Git 识别为一个版本控制仓库,并且会在当前目录下创建一个隐藏的 .git 文件夹,用于存储仓库的元数据信息。  

*git remote add origin + 网址*  
当前 Git 仓库添加一个名为 origin 的远程仓库,并指定其 URL 地址。
这个命令用于将本地仓库与远程仓库进行关联,这样就可以在本地和远程仓库之间进行代码推送和拉取。  

*git pull origin master*  
从名为 origin 的远程仓库的 master 分支上拉取最新的代码更新到本地。
这个命令用于将远程仓库的代码更新拉取到本地,避免在推送代码时出现冲突。

*git add .*  
将当前目录下的所有修改过的文件添加到 Git 的暂存区。
这个命令可以一次性将所有修改过的文件添加到暂存区,为后续的提交做准备。

*git commit -m ''*  
将暂存区的文件内容创建一个新的提交(commit)。
这个命令会创建一个新的提交记录,并附带一段提交说明。提交后,这些修改就正式进入了 Git 仓库的版本历史中。

*git push origin master*  
将当前分支的内容推送到名为 origin 的远程仓库的 master 分支上。
这个命令用于将本地仓库的提交推送到远程仓库,使远程仓库与本地仓库保持同步。  

这里一般git仓库的默认分支为master，如果自己创建了不同命名的分支，需要进行分支的切换。