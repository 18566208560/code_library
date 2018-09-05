`git init`命令把这个目录变成Git可以管理的仓库： 

用命令`git add`告诉Git，把文件添加到仓库： 

用命令`git commit`告诉Git，把文件提交到仓库： 

为什么Git添加文件需要`add`，`commit`一共两步呢？因为`commit`可以一次提交很多文件，所以你可以多次`add`不同的文件， 





`pwd`命令用于显示当前目录 



`git log`可以查看交历史，以便确定要回退到哪个版本。 

`git reflog`查看命令历史，以便确定要回到未来的哪个版本。 

` git reset --hard HEAD^`回退到`add distributed`版本时 

```
 git reset --hard 1094a  #版本号没必要写全，前几位就可以了，Git会自动去找。当然也不能只写前一两位，因为Git可能会找到多个版本号，就无法确定是哪一个了。
```





```
git remote add origin git@github.com:michaelliao/learngit.git
#远程库的名字就是origin
 git push -u origin master
把本地库的内容推送到远程，用git push命令，实际上是把当前分支master推送到远程。
由于远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。
```

从现在起，只要本地作了提交，就可以通过命令：

```
$ git push origin master
```





```
 git clone git@github.com:michaelliao/gitskills.git
 现在，远程库已经准备好了，下一步是用命令git clone克隆一个本地库：
 然后使用git clone命令克隆。

Git支持多种协议，包括https，但通过ssh支持的原生git协议速度最快。
```