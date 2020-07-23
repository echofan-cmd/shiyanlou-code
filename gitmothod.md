在实验楼的code提交到我创建的github仓库中：
github进入方法：
1. 用Googlechrome浏览器进去github网站，用账号密码登录sign in(我已创建账号echofan-cmd,密码github128103，邮箱fxlhv89@163.com,邮箱密码fjb***28)
2. 创建一个新的仓库（方法为：在网页右上角账号信息旁边有个＋号，下拉选择 new a repository，为新仓库起个名字 如：shiyanlou-code,仓库建立后，会出现一个web URL, 用来远程clone仓库到本地的URL，如https://github.com/echofan-cmd/shiyanlou-code.git)
3. 在实验楼的Xfce终端 里 输入如下命令：
  shiyanlou:~/$pwd      #查看当前文件路径  并选择 将web仓库克隆到本地的存放位置
  /home/shiyanlou
  cd Code     #进入Code文件夹
  /home/shiyanlou/Code/$git clone https://github.com/echofan-cmd/shiyanlou-code.git   #git clone +web URL , 即将Web仓库克隆到本地，克隆完成后，cd进入到仓库目录
  shiyanlou:Code/$cd shiyanlou-code
  shiyanlou:shiyanlou-code/(master)$gedit gitmothod.md   #用gedit编辑器新建一个文件，并打开进行内容编辑。
  shiyanlou:shiyanlou-code/(master)$ls     #可查看当前仓库目录下的文件列表
  shiyanlou:shiyanlou-code/(master*)$git add --all    # or   $git add 文件1 文件2 文件3    将列出的文件add到本地仓库目录中，注意 当有未commit提交的文件存在时，master会有个* 标识       参数 all前面有两个-，--all
  shiyanlou:shiyanlou-code/(master*)$git status      #可查看当前仓库状态  ， 可以看到提示 暂存区有文件 且未提交。
其中，使用命令(git reset HEAD <文件>...)以取消暂存
status返回的结果有：
位于分支master
要提交的变更：

	新文件：gitmothod.md

shiyanlou:shiyanlou-code/(master*)$git config --global user.name "echofan-cmd"   #提交文件之前先配置用户名和邮箱
shiyanlou:shiyanlou-code/(master*)$git config --global user.email "fxlhv89@163.com"   #git配置 邮箱
shiyanlou:shiyanlou-code/(master*)$git commit -m "描述说明"   #将之前在暂存区的文件，在本地仓库提交。
shiyanlou:shiyanlou-code/(master*)$git push https://github.com/echofan-cmd/shiyanlou-code.git  #将本地仓库推送到web仓库    $git push 本地仓库名  webURL  若处在本地仓库目录下，本地仓库名 字段可省略
至此，已完成将本地文件上传到web仓库中，登录web github 刷新自己的仓库列表， 可查看到新同步的文件。

### 练习在Web仓库上更新后，克隆到本地仓库，并查看   $git clone https://github.com/echofan-cmd/shiyanlou-code.git

