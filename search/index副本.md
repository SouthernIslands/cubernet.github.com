---
layout: page
title: 搜索
---


<script src="/media/js/jekyll-search.js" type="text/javascript" charset="utf-8"></script>

<div id="search">
  <form action="/search" method="get">
    <input type="text" id="search-this-page" name="q" placeholder="Search.." autocomplete="off">
  </form>
</div>
<ul id="search-results"></ul>

<script type="text/javascript">
        JekyllSearch.init({
          searchInput: document.getElementById("search-this-page"),
          jsonFile : '/search.json',
          searchResults : document.getElementById("search-results"),
          template : '<li><article><a href="{url}">{title} <span><time datetime="{date}">{date}</time></span></a></article></li>',
          fuzzy: true
        });
</script>
