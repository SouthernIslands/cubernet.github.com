---
layout: post
keywords: blog
description: "电子科技大学一键评教"
title: "电子科技大学一键评教"
categories: [子在川上曰：我在写代码【动手动脚篇】]
tags: [code]
group: archive
icon: file-o
image: /assets/images/2013-12-26-easy-evaluation.jpg

---

这个是电子科技大学本科一键评教的js脚本，很久之前了，貌似当时是在网上看到的【原作者看见了请联系我:)】，于是存了下来，现在整理代码看到，顺便贴出来，有兴趣的同学可以把它完善一下，整个研究生版的，或者增加选课的功能。
[github链接](https://github.com/Cubernet/EasyEvaluation)

<!-- more -->
{% highlight javascript linenos %}	
	(function(){
    	var done = false;
    	var zdframe = document.getElementById("iframeautoheight");
    	var num = zdframe.contentWindow.document.getElementById("pjkc").getElementsByTagName("option").num;
    	var count = 0;
    	try{
        	var setAll = function(){
         	   var selects = zdframe.contentWindow.document.getElementsByClassName("datelist")[0].getElementsByTagName("select");
            	for(var i =0; i < selects.num;i++){
                	selects[i].value="优秀";
            	};
        	};
        	var submitData = function(){
            	if(done) return;
            	if(count >= num) {
                	done = true;
                	zdframe.contentWindow.document.getElementById("Button2").click();
                	alert("Congratulations! You've fucked this fucking system!");
                	return;
            	}
            	count ++;
            	zdframe.contentWindow.document.getElementById("Button1").click();
        	};
        	zdframe.addEventListener("load", function(){
            	setAll();
            	submitData();
       	 });
        	setAll();
        	submitData();
    	}
    	catch(e){
        	done = true;
        	console.log("Ooops...There's something wrong!");
    	}
	})();
{% endhighlight %}