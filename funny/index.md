---
layout: page
title: 趣图
---


<script src="/media/js/move.js" type="text/javascript"></script>

<p>如果涉及到版权问题，请及时联系我。</p>

<ul class="parent clear" id="picsul">
    <li></li>
    <li></li>
    <li></li>
</ul>

<script>

        
        var oParent=getByClass('parent')[0];
        
        var aLi=oParent.getElementsByTagName('li');
        var iPage=1;
        var iOpen=true;
        var jsonData = null;

        window.onload = function(){
            var jsonFile = "/pic.json";
                var xhr = (window.XMLHttpRequest) ? new XMLHttpRequest() : new ActiveXObject("Microsoft.XMLHTTP");
                xhr.open("GET", jsonFile, true);
                xhr.onreadystatechange = function(){
                    if (xhr.status==200 && xhr.readyState==4){
                        try{
                            jsonData = JSON.parse( xhr.responseText );
                            console.log( "data loaded successfully" );
                            showList();        //初始化加载第一批图片
                            }catch(err){
                            console.log( err );
                            jsonData = null;
                        }
                    }
                }
                xhr.send(); 
        };


        function fnMove() {        //鼠标经过图片透明度变化
                var aDiv=getByClass('pic');
                for(var i=0;i<aDiv.length;i++) {
                var oImg=aDiv[i].getElementsByTagName('img')[0];
                var bDiv=document.createElement('div');
                var bImg=document.createElement('img');
                var btitle=document.createElement('div');
                        oImg.onmouseover=function() {
                                this.style.filter='alpha(opacity:60)';
                                this.style.opacity=0.6;                                      
                        }
                        oImg.onmouseout=function() {
                                this.style.filter='alpha(opacity:100)';
                                this.style.opacity=1;          
                        }
                        oImg.onclick=function(){
                            bDiv.appendChild(btitle);
                            bDiv.appendChild(bImg);
                                btitle.innerHTML="再次单击关闭大图";
                                bImg.src = this.src;
                                document.getElementById('picsul').appendChild(bDiv);
                                btitle.style.fontSize="12px";
                                btitle.style.color="#333333";
                                btitle.style.height="15px";
                                bDiv.style.backgroundColor="#DDDDDD";
                                bDiv.style.zIndex="2";
                                bDiv.style.position="absolute";
                                bDiv.style.left=document.body.offsetWidth/3;
                                bDiv.style.top=document.body.scrollTop+50;
                                bDiv.style.cssFloat="left"; 
                                bDiv.style.border="solid 1px";
                                bDiv.style.borderColor="#0099ff";
                                bDiv.style.borderRadius="6px";

                                bImg.onclick=function(){
                                  document.getElementById('picsul').removeChild(bDiv);
                                }
                        }
                }
        }
        
        

        window.onscroll=function() {
                
                var _index=        iMin();        //最小高度li的下标
                var oLi=aLi[_index];        //最小高度的li
                var ih=pos(oLi)+oLi.offsetHeight;
                if(ih<(viewH()+scrollY())) {
                        showList();
                }
        };

        function showList() {
                if(!iOpen) return;
                iOpen=false;
                if(!jsonData) return;
                iPage++;

                var i=0;

                function show1() {
                    var oDiv=document.createElement('div');
                    var oImg=document.createElement('img');
                    var oP=document.createElement('p');
                    oDiv.className='pic'; 
                    var j = jsonData.length/2;
                    oP.innerHTML=jsonData[i+j].title || '暂无介绍';                  
                    oDiv.appendChild(oImg);
                    oDiv.appendChild(oP);
                    oImg.src="";
                    aLi[iMin()].appendChild(oDiv);
                    fnMove();//调用经过事件
                    if(jsonData[i].url) {
                        oImages=new Image();
                        oImages.onload=function() {
                        oImg.src=this.src;
                        oImg.style.filter='alpha(opacity:0)';        //图片加载完成时，进行透明度变化
                        oImg.style.opacity=0;
                        startMove(oImg,{
                        opacity:100        
                        });        
                        if(i<jsonData.length/2-1) {
                            i++;
                            show1();        
                        }else {
                            iOpen=false;        
                        }
                      }
                        oImages.src=jsonData[i].url;                                               
                    }else {                                //当图片加载失败走这里
                        if(i<jsonData.length/2-1) {        
                            i++;
                            show1();        
                        }else {
                            iOpen=false;        
                        }
                    }        
                                                        
                }
            show1();
                                              
        }

        
        

        //函数封装
        function iMin() {
                var ih=aLi[0].offsetHeight;
                var _index=0;
                for(var i=1;i<aLi.length;i++) {
                        if(ih>aLi[i].offsetHeight) {
                                ih=aLi[i].offsetHeight;
                                _index=i;        
                        }
                }
                return _index;
        }

        function getByClass(sClass,parent) {
                var aEle=(parent || document).getElementsByTagName('*')
                var arr=[];
                var re=new RegExp('\\b' + sClass + '\\b');
                for(var i=0;i<aEle.length;i++) {
                        if(re.test(aEle[i].className)) {
                                arr.push(aEle[i]);        
                        }
                        
                }
                return arr;
        }
        
        function pos(obj) {
                var iTop=0;        
                while(obj) {
                        iTop +=obj.offsetTop;
                        obj=obj.offsetParent;
                }
                return iTop;
                
        }
        function viewH() {
                return document.documentElement.clientHeight;        
        }
        function scrollY() {
                return document.documentElement.scrollTop || document.body.scrollTop;        
        }

        
</script>
