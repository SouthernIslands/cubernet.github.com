---
title: 阅读书单
layout: page
comments: yes
---


<h2 class="archive-title">阅读书单</h2>

<article class="page"> 
<div class="post-content">
<div class="entry">
<p><img src="/assets/images/books.jpg" alt="image"></p>
<blockquote>书犹药也，善读之可以医愚。——刘向
</blockquote>
<p>做这个阅读书单的想法是从一位素未谋面的博主那里“窃”来的。我觉得这种方式很好，一来可以把我读过的好书推荐给大家，二来可以记录自己读过多少书，进而从数量的角度激励自己读更多。</p>
<p>我喜欢读书。这里所谓的读书并非仅指做学问。书有很多种，我向来推荐各种书都读。正如开头引用刘向所言，多读书未必会使你算术一流、聪明过人，但书会使一个人变的睿智。有了这种睿智，日常的言谈举止、为人处世都会有不一样的境界。</p>
<p>这是个过程，需要积淀。</p>
<p>最后欢迎大家留言推荐好看的书。</p>
<p>我读的书少，你们不要骗我。</p>
<p></p>
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
{% if cat[0] == '阅读书单' %}
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





