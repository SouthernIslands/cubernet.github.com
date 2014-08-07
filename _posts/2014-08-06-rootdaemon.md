---
layout: post
title: "【译】在iOS上以root身份运行守护进程"
description: "【译】在iOS上以root身份运行守护进程 翻译《Run a daemon (as root) on iOS》"
categories: [众里寻他千百度，蓦然回首，那人正在写代码【他山之石篇】]
tags: [iOS,Theos,System Security,daemon]

---

![image](/assets/images/2014-08-06-rootdaemon.png)

[原文地址](http://bbs.iosre.com/forum.php?mod=viewthread&tid=204&page=1&extra=#pid1096)：http://bbs.iosre.com/forum.php?mod=viewthread&tid=204&page=1&extra=#pid1096

作者：snakeninny

感谢snakeninny提供的优质文章。

这篇文章在我最近项目的完成过程中给予了很大的帮助，特在此表示感谢，并翻译之。

<!-- more -->
下面是译文内容：

##第一部分 基础理论

1. 守护进程
	
	什么是守护进程？根据[wikipedia](http://http:en.wikipedia.org/wiki/Daemon)的解释，守护进程是一个运行在计算机后台、不受前台用户交互影响的进程。通常，守护进程的以字母`d`结尾，例如，syslogd是处理系统日志的后台进程，sshd是处理SSH链接请求服务的进程。你可以以`backboardd`,`mediaserverd`,`apsd`等 来命名iOS上的其他后台进程。 后台进程是由iOS上的第一个进程`launchd`启动的，launchd是开机时启动的第一个进程。那么守护进程能做什么呢？“它可以为网络请求，硬件活动以及一些处理其他任务的程序提供后台服务”。**注意：以root身份运行的后台进程功能非常强大，并且非常隐蔽，很多时候也许超级管理员都不知道有一些后台进程在偷偷运行。所以，一些恶意软件就是以后台进程的形式存在的。这篇文章只是用来交流学习，如果你去做非法的事情，后果自负。**
	
2. 守护进程的所有者

	守护进程是由launchd启动，通过“launchctl”命令加载配置文件。我们要特别注意在这个[查询手册](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/launchctl.1.html)中提到的，“LaunchAgents启动加载的每个配置文件必须属于启动加载它们的用户。所有的系统后台进程必须属于root用户。”配置文件不可以是属于“group-”或者任何人可写。这些限制是出于安全考虑，因为如果一个启动配置文件是任何人可写的话，那么就有可能出现在程序启动时配置文件被恶意修改的情况。因为后台进程是由launchd启动的，所以它应该属于root:wheel：
		
		FunMaker-5:~ root# ls -l /sbin/launchd
		-r-xr-xr-x 1 root wheel 154736 Nov  8  2013 /sbin/launchd
		
##第二部分 组成

正如在《iOS应用逆向工程》一书中提到的那样，后台进程包括两个部分，一个可执行的二进制文件和一个配置plist配置文件。下面，让我们利用Theos来创建一个可执行二进制文件：

	snakeninnys-MacBook:Code snakeninny$ /opt/theos/bin/nic.pl
	NIC 2.0 - New Instance Creator
	------------------------------
  	[1.] iphone/application
  	[2.] iphone/cydget
  	[3.] iphone/framework
  	[4.] iphone/library
  	[5.] iphone/notification_center_widget
  	[6.] iphone/preference_bundle
  	[7.] iphone/sbsettingstoggle
  	[8.] iphone/tool
  	[9.] iphone/tweak
  	[10.] iphone/xpc_service
	Choose a Template (required): 8
	Project Name (required): rootdaemond
	Package Name [com.yourcompany.rootdaemond]: com.iosre.rootdaemond
	Author/Maintainer Name [snakeninny]: snakeninny
	Instantiating iphone/tool in rootdaemond/...
	Done.
	
然后修改main.mm文件的内容：

	static void Reboot(CFNotificationCenterRef center, void *observer, CFStringRef name, const 	void *object, CFDictionaryRef userInfo)
	{
        	NSLog(@"iOSRE: reboot");
        	system("reboot");
	}
	
	int main(int argc, char **argv, char **envp)
	{
        	NSLog(@"iOSRE: rootdaemond is launched!");
        	CFNotificationCenterAddObserver(CFNotificationCenterGetDarwinNotifyCenter(), NULL, Reboot, CFSTR("com.iosre.rootdaemon.reboot"), NULL, 	CFNotificationSuspensionBehaviorCoalesce);
        	CFRunLoopRun(); // keep it running in background
        	return 0;
	}
	
现在，让我们处理配置文件。以“com.iosre.rootdaemond.plist”为文件名新建文件，然后将下面的代码写入文件中：

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/	PropertyList-1.0.dtd">
	<plist version="1.0">
	<dict>
        	<key>KeepAlive</key>
        	<true/>
        	<key>Label</key>
        	<string>com.iosre.rootdaemond</string>
        	<key>Program</key>
        	<string>/usr/bin/rootdaemond</string>
        	<key>RunAtLoad</key>
        	<true/>
	</dict>
	</plist>
	
在这些键值对当中，`Label`键对应的是一个可以唯一标示你的后台进程的字符串，`Program`键对应的是可执行文件所在位置的绝对路径，这两个都是必填的。如果你的后台进程还有其他的参数，那么只需要在文件中增加类似下面这样的键值对即可：

	<key>ProgramArguments</key>
   	 <array>
        	<string>arg1</string>
        	<string>arg2</string>
        	<string>more args...</string>
    	</array>
    	
在完成了这些之后，我们把这个配置文件保存在项目根目录下的/layout/Library/System/文件夹中。现在，我们的项目树看上去是这个样子的：

![image](/assets/images/2014-08-06-rootdaemon2.png)

执行`make package`命令，然后检查deb所属的用户：
	
	snakeninnys-MacBook:rootdaemond snakeninny$ dpkg-deb -c /Users/snakeninny/Code/	rootdaemond/com.iosre.rootdaemond_1.0-1_iphoneos-arm.deb 
	drwxr-xr-x snakeninny/staff  0 2014-05-11 15:52 ./
	drwxr-xr-x snakeninny/staff  0 2014-05-11 14:45 ./Library/
	drwxr-xr-x snakeninny/staff  0 2014-05-11 15:48 ./Library/LaunchDaemons/
	-rwxr-xr-x snakeninny/staff 367 2014-05-11 15:37 ./Library/LaunchDaemons/	com.iosre.rootdaemond.plist
	drwxr-xr-x snakeninny/staff   0 2014-05-11 15:52 ./usr/
	drwxr-xr-x snakeninny/staff   0 2014-05-11 15:52 ./usr/bin/
	-rwxr-xr-x snakeninny/staff 197984 2014-05-11 15:52 ./usr/bin/rootdaemond

可以看到，deb中的所有文件都是属于snakeninny:staff的。还记得在第一部分中提到，后台进程必须属于root用户吗？所以，这个后台进程所属的用户不对，当你运行时将会报错。

这是为什么呢？因为这个deb文件是在OSX上打包的，所以它所属的用户就是snakeninny。为了将它的所属用户改为root:wheel，我们需要一个叫做[fauxsu](https://github.com/DHowett/fauxsu)的工具。下载这个工具，将解压得到的fauxsu和libfauxsu.dylib复制到`$THEOS/bin/` 目录下，然后运行`chmod a+x`。重新打包检查一次：

	snakeninnys-MacBook:rootdaemond snakeninny$ dpkg-deb -c /Users/snakeninny/Code/	rootdaemond/com.iosre.rootdaemond_1.0-2_iphoneos-arm.deb 
	drwxr-xr-x root/wheel        0 2014-05-11 16:05 ./
	drwxr-xr-x root/wheel        0 2014-05-11 14:45 ./Library/
	drwxr-xr-x root/wheel        0 2014-05-11 15:48 ./Library/LaunchDaemons/
	-rwxr-xr-x root/wheel      367 2014-05-11 15:37 ./Library/LaunchDaemons/	com.iosre.rootdaemond.plist
	drwxr-xr-x root/wheel        0 2014-05-11 16:05 ./usr/
	drwxr-xr-x root/wheel        0 2014-05-11 16:05 ./usr/bin/
	-rwxr-xr-x root/wheel   197984 2014-05-11 16:05 ./usr/bin/rootdaemond

现在，文件所属用户是正确的了。执行`make install`来安装这个后台进程：

	snakeninnys-MacBook:rootdaemond snakeninny$ make install
	install.exec "cat > /tmp/_theos_install.deb; dpkg -i /tmp/_theos_install.deb && rm /tmp/	_theos_install.deb" < "./com.iosre.rootdaemond_1.0-2_iphoneos-arm.deb"
	Selecting previously deselected package com.iosre.rootdaemond.
	(Reading database ... 2589 files and directories currently installed.)
	Unpacking com.iosre.rootdaemond (from /tmp/_theos_install.deb) ...
	Setting up com.iosre.rootdaemond (1.0-2) ...
	
##第三部分 测试

重启手机检查后台进程是否启动：

	FunMaker-5:~ root# reboot
	FunMaker-5:~ root# Connection to 192.168.1.101 closed by remote host.
	Connection to 192.168.1.101 closed.
	snakeninnys-MacBook:Code snakeninny$ ssh root@192.168.1.101
	FunMaker-5:~ root# grep iOSRE /var/log/syslog
	May 11 16:14:01 FunMaker-5 rootdaemond[20]: iOSRE: rootdaemond is launched!
	FunMaker-5:~ root# ps -e | grep rootdaemond
 	  20 ??         0:00.13 /usr/bin/rootdaemond
  	370 ttys000    0:00.01 grep rootdaemond
	FunMaker-5:~ root#
	
我们可以看到，rootdaemond开机自动启动，并且保持在后台运行。最后，我们检查一下它是否在像预期的那样运行：

	// compile: clang -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS7.0.sdk -o iOSRERootDaemonTester -arch armv7 /Users/snakeninny/main.mm

	#include <notify.h>

	int main(int argc, char **argv)
	{
        	notify_post("com.iosre.rootdaemon.reboot");
        	return 0;
	}
	
用scp命令将iOSRERootDaemonTester复制到iOS上，然后运行：

	snakeninnys-MacBook:~ snakeninny$ scp iOSRERootDaemonTester root@192.168.1.101:/var/tmp/
	iOSRERootDaemonTester                         100%   48KB  48.3KB/s   00:00    
	FunMaker-5:~ root# /var/tmp/iOSRERootDaemonTester
	FunMaker-5:~ root# Connection to 192.168.1.101 closed by remote host.
	Connection to 192.168.1.101 closed.
	snakeninnys-MacBook:Code snakeninny$ ssh root@192.168.1.101
	FunMaker-5:~ root# grep iOSRE /var/log/syslog
	May 11 16:36:01 FunMaker-5 rootdaemond[20]: iOSRE: reboot
	May 11 16:36:58 FunMaker-5 rootdaemond[20]: iOSRE: rootdaemond is launched!
	FunMaker-5:~ root#
	
它神奇的运行了。

##第四部分 结论

事实上，在iOS或者OSX上，后台进程和代理程序远比这篇文章中描述的要复杂的多。我强烈建议大家看一下下面相关的文章。再次强调，后台进程是一个强大的工具，但它是一把双刃剑，在你决定使用它之前，你最好非常了解自己接下来将要做什么，然后小心的使用它。谢谢阅读。

相关阅读：

1. http://en.wikipedia.org/wiki/Daemon_(computing)
2. https://www.chrisalvares.com/blog/7/creating-an-iphone-daemon-part-1/
3. https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/launchctl.1.html
4. https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html
5. https://developer.apple.com/library/mac/documentation/Darwin/Reference/Manpages/man5/launchd.plist.5.html

2014.5.22注：
com.iosre.rootdaemond.plist文件必须拥有644权限，否则示例后台进程将不会运行。









