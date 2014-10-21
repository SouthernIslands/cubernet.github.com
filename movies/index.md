---
title: 观影列表
layout: page
comments: yes
---


<h2 class="archive-title">观影列表</h2>

<article class="page"> 
<div class="post-content">
<div class="entry" style="text-align:center">
<p><img src="/assets/images/movies.jpg" alt="image"></p>
<p>学习之余，一场电影，就是一次彻底的放空；</p>
<p>或欢乐，或感动，或震撼，或沉思；</p>
<p>我在这里记录我的分享；</p>
<p>也在这里等待你的推荐。</p>
</div>
<footer>
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
  <a class="jiathis_button_weixin">微信</a>
  <a class="jiathis_button_qzone">QQ空间</a>
  <a class="jiathis_button_tsina">新浪微博</a>
  <a href="http://www.jiathis.com/share?uid=1954501" class="jiathis jiathis_txt jiathis_separator jtico jtico_jiathis" target="_blank">更多</a>
</div>
<script type="text/javascript">
var jiathis_config = {data_track_clickback:'true'};
</script>
<script type="text/javascript" src="http://v3.jiathis.com/code_mini/jia.js?uid=1954501" charset="utf-8"></script>
<!-- JiaThis Button END -->
</footer>
</div>
</article>

{% for cat in site.categories %}
{% if cat[0] == '观影列表' %}
{% for post in cat[1] %}
<div class="archive">
<article class="post">
<div class="post-content">
<header>
<h1 class="title">
<a href="{{ post.url }}">{{ post.title }}</a>
</h1>
</header>
</div>
</article>
</div>
{% endfor %}
{% endif %}
{% endfor %}