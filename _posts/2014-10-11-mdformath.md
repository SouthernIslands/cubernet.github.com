---
layout: post
title: "在Markdown中使用数学公式"
description: "markdown latex"
categories: [子在川上曰：我在写代码【动手动脚篇】]
tags: [LaTex]
music: []

---

![image](/assets/images/2014-10-11-mdformath.jpg)

上一博文是翻译的一篇学术论文，在用markdown语法编辑译文时，发现原文中出现的公式不知如何插入。

当然，能想到的一个简单的办法就是，把原文中的公式截图，然后在译文中插入图片。但是，作为一个天生爱折腾的工科男，这样的解决办法显然满足不了我。

<!-- more -->

用百度谷歌了一番之后发现，原来还真有别的办法。那就是将LaTex强大的数学公式排版能力与Markdown相结合。

第一步，将原文中的公式用Latex语法描述出来。例如![image](http://latex.codecogs.com/png.latex?\\\I\(x;y\)%20=%20\iint%20p\(x,y\)log\frac{p\(x,y\)}{p\(x\)p\(y\)}dxdy.)这个公式的Latex语法是：`I(x;y\)=\iint p(x,y)log\frac{p(x,y)}{p(x)p(y)}dxdy.`

第二步，将这段LaTex语法描述的公式转化成图片插入到Markdown文本中。这里有两个可以调用的接口。

七十二松网站的Latex服务调用接口：

>http://tex.72pines.com/latex.php?latex=$LaTeX公式代码$

Google的Latex服务调用接口：

>http://latex.codecogs.com/png.latex?LaTex公式代码

当然，看到这里，有些同学可能会说，用LaTex语法编写数学公式的门槛太高，需要太多时间去熟悉、记忆。其实你大可不必担心，推荐给大家一个很好的在线LaTex公式编辑器，[**传送门**](http://latex.codecogs.com/)。有了它，分分钟写出自己想要的LaTex公式不是梦。当然，这个网站也提供了丰富易用的调用接口，大家也可以直接利用。

---

还有一种方法我没有尝试，但是整理在这里，供大家参考。其实也很简单，那就是使用[**MathJax**](http://www.mathjax.org)，只需要在你的页面添加几行代码，就可以解析LaTex、MathML等语法描述的数学公式了。如果你用过，欢迎与我交流使用感受<img src="http://cubernet.cn/assets/smilies/16.gif"id="smiley">。










