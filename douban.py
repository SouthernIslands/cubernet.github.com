#coding=utf-8
import urllib2,re,os,urllib,sys,string,threading,Queue,socket,cookielib
from django.template.defaultfilters import title

def readsrc(src):
    try:
        url = urllib2.urlopen(src)
        content = url.read()
        return content
    except:
        print 'readsrc error'
        return None

def searchMovie(name):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    host = 'movie.douban.com'
    cookie = 'bid="uy1m8iUBqmw"; __utma=30149280.1311490216.1399965921.1413917311.1413951356.5; __utmz=30149280.1402501019.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E7%A7%BB%E5%8A%A8webapp; ll="118327"; _pk_id.100001.4cf6=b5464b80bbeb36e3.1413917311.2.1413952310.1413917584.; __utmc=30149280; __utma=223695111.1687425709.1413917311.1413917311.1413951356.2; __utmc=223695111; __utmz=223695111.1413917311.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); viewed="25985499"; __utmb=30149280.4.10.1413951356; __utmb=223695111.4.10.1413951356; _pk_ses.100001.4cf6=*; __utmt_douban=1; __utmt=1'
    headers = { 'Host':host,'User-Agent' : user_agent, 'Accept-Language': ':zh-CN,zh;q=0.8,en;q=0.6' ,'cookie':cookie} 
    data = ''
    req = urllib2.Request('http://movie.douban.com/subject_search?search_text='+name, data, headers)
    response = urllib2.urlopen(req)
    web_page = response.read()
    
    return web_page

def getMovieUrl(content):
    p = re.compile(r'http://movie.douban.com/subject/(.*?)/',re.M)
    r = p.findall(content)
    if r:
        return 'http://movie.douban.com/subject/'+r[0]
    else:
        return None
    
def getDetailPage(url):
    try:
        url = urllib2.urlopen(url)
        content = url.read()
        return content
    except:
        print 'readsrc error'
        return None  
    
def getDirector(content):
    p = re.compile(r'<a href=.*?rel="v:directedBy">(.*?)</a>',re.M)
    r = p.findall(content)
    if r:
        return r[0]
    else:
        return None
def getLeader(content):
    p = re.compile(r'<a href=.*?rel="v:starring">(.*?)</a>',re.M)
    r = p.findall(content)
    if r:
        return r
    else:
        return None
    
def getType(content):
    p = re.compile(r'<span property="v:genre">(.*?)</span>',re.M)
    r = p.findall(content)
    if r:
        return r
    else:
        return None

def getPoster(content):
    p = re.compile(r'<img src="http://img\d.douban.com/view/.*?/p(\d*).jpg".*?rel="v:image".*?>',re.M) 
    r = p.findall(content)
    if r:
        return 'http://img3.douban.com/view/photo/photo/public/p'+r[0]+'.jpg'
    else:
        return None

def getCoverUrl(url,name):  
    f = open('/Users/Cubernet/Documents/githubblog/cubernet.github.com/assets/posters/'+name+'.jpg',"wb")
    f.write(readsrc(url))
    f.close()
    
    return '/assets/posters/'+name+'.jpg'

if __name__=='__main__':   
    if sys.argv[1].startswith('--'):  
        option = sys.argv[1][2:]  
        if option == 'help':  
            print '''
            -----------------------------------------------------------

            This program downloads movie information from www.douban.com. 
            Options include:  
              --help    : Display this help
              -y[<year>]            : The year of this movie showed
              -n[<vol number>]      : The name that you want to search
              -p[<filepath>]        : The name of the poster
              -d[<description>]     : The description of thie movie

            -----------------------------------------------------------
              '''    
    elif sys.argv[1].startswith('-'):
        year = sys.argv[2]
        name = sys.argv[4]
        postername = sys.argv[6]
        if len(sys.argv) > 7:
            description = sys.argv[8]
        else:
            description = '暂无影评'
        link = getMovieUrl(searchMovie(name))
        pageContent = getDetailPage(link)
        director =  getDirector(pageContent)
        leaders = getLeader(pageContent)
        movietype = getType(pageContent)
        posterurl = getPoster(pageContent)
        status = '已看'
        cover = getCoverUrl(posterurl, year+'_'+postername)
           
        print 'title==>'+name+'\n'
        print 'director==>'+director+'\n'
        for leader in leaders:
            print 'leaders==>'+leader+'\n'
        for mytype in movietype:
            print 'movietype==>'+mytype+'\n'
        print 'link==>'+link+'\n'
        
        f = open('/Users/Cubernet/Documents/githubblog/cubernet.github.com/_posts/'+year+'-01-01-movie_list_'+year+'.md',"rb")
        list_of_all_the_lines = f.readlines( )
        mylist = list_of_all_the_lines[:-1]
        f.close()
        f = open('/Users/Cubernet/Documents/githubblog/cubernet.github.com/_posts/'+year+'-01-01-movie_list_'+year+'.md',"wb")
        mylist.append('    - title : '+name+'\n')
        mylist.append('      director : '+director+'\n')
        if (len(leaders)==1):     
            mylist.append('      leader : '+leaders[0]+'\n') 
        else:
            for num in range(len(leaders)):
                if(num==0):
                    mylist.append('      leader : '+leaders[num]+'/')  
                elif(num<3) and (num == len(leaders)-1):
                    mylist.append(leaders[num]+'\n')
                elif(num==3):
                    mylist.append(leaders[num]+'\n')
                elif(num>3):
                    break
                else:
                    mylist.append(leaders[num]+'/')  
        if (len(movietype)==1):     
            mylist.append('      type : '+movietype[0]+'\n') 
        else:
            for num in range(len(movietype)):
                if(num==0):
                    mylist.append('      type : '+movietype[num]+'/')
                elif(num<3) and (num == len(movietype)-1):
                    mylist.append(movietype[num]+'\n')
                elif(num==3):
                    mylist.append(movietype[num]+'\n')
                elif(num>3):
                    break
                else:
                    mylist.append(movietype[num]+'/')
        mylist.append('      link : '+link+'\n')
        mylist.append('      status : '+status+'\n')
        mylist.append('      description : '+description+'\n')
        mylist.append('      cover : '+cover+'\n')
        mylist.append('---')
        f.writelines(mylist)
        f.close()
        sys.exit()
        
        
        





