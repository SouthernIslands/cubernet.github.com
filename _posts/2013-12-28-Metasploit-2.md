---
layout: post
keywords: blog
description: "Metasploit渗透测试相关(一)——Metasploit相关"
title: "Metasploit渗透测试相关(一)——Metasploit相关"
categories: [learning, Metasploit]
tags: [Metasploit,渗透]
group: archive
icon: file-o

---

![image](/assets/images/2013-12-28-Metasploit-2.png)

>Metasploit项目（Metasploit Project）是一个旨在提供安全漏洞信息（Vulnerability Information）计算机安全项目，可以协助安全工程师进行渗透测试（penetration testing）及入侵检测系统签名开发。

>Metasploit项目最为知名的子项目是开源的Metasploit框架（Metasploit Framework），一套针对远程主机进行开发和执行“exploit代码（exploit code）”的工具。其他重要的子项目包括Opcode数据库、shellcode档案、安全研究等内容。

>Metasploit项目知名的功能还包括反取证（anti-forensic）与规避工具（evasion tools），其中的某些工具已经内置在Metasploit Framework里面。

>——维基百科

<!-- more -->

这一节的内容多为从`《Metasploit用户指南》`中摘取出来的，感兴趣的朋友可以去阅读完整版。

---
#### 安装

##### 在windows上的安装
1、访问http://www.metasploit.com/download/下载Windows的安装文件。

2、找到下载好的安装文件并双击安装程序的图标。此时可能会出现安全警告。在安全警告界面上点击“运行（Run）”。当安装欢迎界面出现之后，点击“下一步（Next）”来继续。在Windows 7上，在出现最初安装界面之前可能需要10分钟时间。

3、接受许可协议书。

4、在你已经阅读并接受许可协议之后点击“下一步（Next）”继续。

5、选择一个安装Metasploit Framework的文件夹。在接下来的界面中，你可以选择安装在默认的文件夹下面或者单击文件夹图标来选择一个不同的目录或者硬盘驱动器。注意选择的目录必须是空目录。

6、点击“下一步（Next）”。

7、输入SSL端口号。

8、输入网络服务器名称来得到一个SSL证书，以使得浏览器运行来匹配其信息。

9、在“有效的天数（Days of validity）”区域中输入证书的有效期的天数。

10、点击“下一步（next）”以继续。此时可能出现一个防火墙的警告，接受其警告以继续。

11、此时会出现一个提醒你已经准备好安装Metasploit Framework的对话框。点击“下一步（Next）”以安装Metasploit Framework及其依赖文件。下个界面会运行接下来的安装程序。安装对话框显示着安装的进度。

12、当安装完成之后，点击“完成（Finish）”按钮。

##### 在linux上的安装
1、访问http://www.metasploit.com/download/下载Linux 32 bit或者64 bit安装包。保存安装文件到一个位置，比如可以放到桌面上。

2、打开一个终端。

3、改变执行安装包的模式。可以由以下命令实现：
	
	对于64位的系统：
	 	chmod +x desktop/metasploit-latest-linux-x64-installer.run
	对于32位的系统：
	 	chmod +x desktop/metasploit-latest-linux-x32-installer.run

4、运行安装包。可以由以下命令实现：

	对于64位系统：
		sudo desktop/metasploit-latest-linux-x64-installer.run
	对于32位系统：
		sudo desktop/metasploit-latest-linux-x32-installer.run

5、如果提示输入密码，请输入你的sudo密码。

6、安装界面出现之后，点击Forward开始安装。

7、接受协议并点击Forward。

8、选择一个安装文件夹然后点击Forward。

9、选择Yes注册Metasploit服务（推荐）。然后点击Forward。

10、输入Metasploit服务使用的端口号。默认的端口号是3790。点击Forward继续。

11、输入用来生成SSL证书的服务器名称。

12、输入希望SSL证书保持有效的天数。点击Forward继续。

13、输入thin服务器的端口号。默认为3000。点击Forward继续。

14、如果想要自动更新开发快照，选择Yes。点击Forward继续。

15、Ready to Install窗口出现。点击Forward开始安装进程。

---


