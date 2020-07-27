# Git
## 取得Git仓库的方法：
1. git init（会创建一个.git的子目录）
2. git clone [url] projectname，自定义projectname
## 记录更新到仓库
1. 检测文件状态 git status
2. 提交到暂存区 git add filename, git add *, git add *.txt
3. 忽略文件 .gitignore
4. 提交更新git commit -m “代码提交信息”
5. 跳过提交暂存区直接更新 git commit -a -m “代码提交信息”
6. 移除文件 git rm filename
7. 重命名 git mv README.md README
## 推送改动到远程仓库
git remote add origin <server>将仓库连接到远程服务器
git push origin master提交改动到远端服务器 master可换
git remote rename test test1 将test重命名为test1
git remote rm test1 移除test1
## 查看历史记录
git log （git log --author==bob）
## 撤销提交
git commit -amend
## 分支
git brunch test 创建test分支
git checkout test 切换到test分支
git merge test 合并test分支
git brunch -丶 删除
#学习/测试