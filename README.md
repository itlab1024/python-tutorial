# Python安装

打开官网https://www.python.org，根据下图进行安装（Mac版）

![image-20221020182444152](https://itlab1024-1256529903.cos.ap-beijing.myqcloud.com/202210201824425.png)

点击Downloads进入

![image-20221020182707072](https://itlab1024-1256529903.cos.ap-beijing.myqcloud.com/202210201827127.png)

windows用户注意

![image-20221020182906540](https://itlab1024-1256529903.cos.ap-beijing.myqcloud.com/202210201829611.png)

mac用户同理选择合适的安装器下载。

![image-20221020183026203](https://itlab1024-1256529903.cos.ap-beijing.myqcloud.com/202210201830274.png)

下载完毕后开始安装，安装过程中一路下一步即可。

安装完毕后检查是否成功。

打开终端

```shell
➜  ~ python3
Python 3.10.8 (v3.10.8:aaaf517424, Oct 11 2022, 10:14:40) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

没问题。

# 开发工具

开发工具我推荐使用Jebrains的PyCharm。下载地址https://www.jetbrains.com/pycharm/

![image-20221020184131000](https://itlab1024-1256529903.cos.ap-beijing.myqcloud.com/202210201841074.png)

安装过程就省略了。

# 创建项目

打开PyCharm，按照图片上说明设置项目信息，并创建项目。

![image-20221020192028791](https://itlab1024-1256529903.cos.ap-beijing.myqcloud.com/202210201920885.png)

**创建一个python文件**

鼠标放到项目名称上，邮件选择New，再选择Python File。输入文件名即可创建一个文件。

# 工具编码设置

设置PyCharm的编码，保证文件的编码都是UTF-8，会避免很多问题。

![image-20221020193653998](https://itlab1024-1256529903.cos.ap-beijing.myqcloud.com/202210201936065.png)

![image-20221020193717061](https://itlab1024-1256529903.cos.ap-beijing.myqcloud.com/202210201937131.png)

# 开始

首先来以为项目入口函数开始，每种语言都会介绍的hello world，对python有个基本的认识。

```python
if __name__ == '__main__':
    print("hello world")
```

额，学过java和go，python设这是啥语法。。。