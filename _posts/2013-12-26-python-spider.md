---
layout: post
keywords: blog
description: blog
title: "Python应用の简单的爬虫"
categories: [python, code]
tags: [python]
group: archive
icon: file-o

---

如果想实现一个简单的爬虫，我想Python一定是最容易上手的。这里就介绍一下如何用Python实现一个简单的爬虫。

![image](/assets/images/2013-12-26-python-spider.jpg)

爬虫最主要的处理对象就是url，其通常的工作流程就是通过给定的入口url爬取网页内容，然后从得到的网页中寻找下一级的url，接着继续重复以上的工作，直到达到包含所需内容的页面，提取到我们关心的数据。

>网络蜘蛛（Web spider）也叫网络爬虫（Web crawler），指的是“自动化浏览网络”的程序，是网络机器人的一种。这样的电脑程序是为了自动从网络截取特定的数据，或为了组织网络上的数据，所设计的“‘自动浏览网络’的程序”。——维基百科

所以，我们需要用到哪些知识就很显而易见了。

<!-- more -->

---

#### 首先，我们要知道如何使用Python获取特定url对应的网页内容。

最简单的，向特定url发送get请求，获取网页内容：

{% highlight python linenos %}

import urllib2
def readsrc(src):
#获取src网址对应的html代码
    try:
        content = urllib2.urlopen(src).read()
        return content
    except URLError,e:
        print e.code
        return None
        	
{% endhighlight %}
        	
  
有时候服务器会通过http报文的header来判断你是不是一个真正的‘human’，所以需要给你的发送的报文添加一个浏览器标示，来简单的迷惑服务器。同时，很多情况下我们需要通过发送post请求来传递更多的数据，那么可以这么写：

{% highlight python linenos %}

from urllib import urlopen
import urllib2

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
headers = { 'User-Agent' : user_agent, 'Accept-Language': ':zh-CN,zh;q=0.8,en;q=0.6' } 
data = '' 
	
req = urllib2.Request(geturl2, data, headers)    
response = urllib2.urlopen(req)    
web_page = response.read() 
	
{% endhighlight %}
	
	
如果你的爬虫想爬取的网站需要先登录才可以继续浏览，这个时候你就需要通过处理cookies等字段来维持爬虫保持`登录`状态。

{% highlight python linenos %}

import urllib    
import urllib2  
import cookielib  
  
cookie = cookielib.CookieJar()    
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  
  
#需要POST的数据#  
postdata=urllib.urlencode({    
'name':'Cubernet',    
'pwd':'Oppos...'    
})  
	  
#自定义一个请求#  
req = urllib2.Request(    
url = 'http://cubernet.me/login.php',    
data = postdata  
) 
	   
#访问该链接#  
result = opener.open(req）
	
{% endhighlight %}


---

#### Http异常处理

服务器上每一个HTTP的应答对象response都包含一个数字"状态码"。上面例1中的代码如果出现异常，则会把http异常的状态码答应出来，常见的404等。

HTTP状态码通常分为5种类型，分别以1～5五个数字开头，由3位整数组成：

	200：请求成功      处理方式：获得响应的内容，进行处理 
	201：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到    	处理方式：爬虫中不会遇到 
	202：请求被接受，但处理尚未完成    处理方式：阻塞等待 
	204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。    处理方式：丢弃
	300：该状态码不被HTTP/1.0的应用程序直接使用， 只是作为3XX类型回应的默认解释。存在多个可用的被请求资源。    处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃
	301：请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL来访问此资源    处理方式：重定向到分配的URL
	302：请求到的资源在一个不同的URL处临时保存     处理方式：重定向到临时的URL 
	304 请求的资源未更新     处理方式：丢弃 
	400 非法请求     处理方式：丢弃 
	401 未授权     处理方式：丢弃 
	403 禁止     处理方式：丢弃 
	404 没有找到     处理方式：丢弃 
	5XX 回应代码以“5”开头的状态码表示服务器端发现自己出现错误，不能继续执行请求    处理方式：丢弃
	
---

#### 知道了如何获取网页内容，接下来需要做的工作就是如何从爬取到的网页代码中找到自己需要的下级url。

很显然，这里我们需要用到`正则表达式`这个神奇的工具。

很多时候我们可能觉得正则很鸡肋，学起来知识点比较琐碎，但又没有很明显的用武之地。网上对正则有一个很形象的比喻，“匕首”。所谓匕首，即它不像十八般武器那么炫酷，但是在关键时刻却能起到意想不到的效果。

这里只介绍Python正则表达式中最常用最简单的一种，想更进一步了解的同学可以查阅一下资料，网上有很多总结的不错，我这里就不赘述啦：）

`re.compile(strPattern[, flag]):`

这个方法是Pattern类的工厂方法，用于将字符串形式的正则表达式编译为Pattern对象。

第二个参数flag是匹配模式，取值可以使用按位或运算符'|'表示同时生效，比如re.I | re.M。

另外，也可以在regex字符串中指定模式。比如`re.compile('pattern', re.I | re.M)`与`re.compile('(?im)pattern')`是等价的。可选值有：

	re.I(IGNORECASE)		忽略大小写
	re.M(MULTILINE)			多行模式
	re.S(DOTALL)			点任意匹配模式
	re.L(LOCALE)			使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
	re.U(UNICODE)			使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
	re.X(VERBOSE)			详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。
	
---

最后，想要让你的爬虫足够机智，你必须赋予它灵活的逻辑判断和高效的正则表达式。个人认为赋予爬虫什么样的逻辑才是一个写爬虫真正的精华和难点所在。而这些又是只能依靠个人经验去提升和摸索的。所以还是要多写多练手。

当然，你可以通过增加代理、设置超时、伪装浏览器、反“盗链”等多种手段来提升爬虫的战斗力，但，逻辑依然是它的灵魂所在。





