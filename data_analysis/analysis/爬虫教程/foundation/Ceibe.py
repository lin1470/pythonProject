# _*_ coding:utf-8 _*_
import requests
import re
import os

###############################作者 ： 李钇廷 ##############################################
#################################用时：4天 #################################################
#############################无界面，输入用户名密码直接爬取###################################
###############################本次更新了某课程，某文件######################################
#################################简单用户名#################################################

pattern = re.compile('<input type=.hidden. name=.lt.*?value=.(.*?).>')
pattern2 = re.compile('<input type=.hidden. name=.execution.*?value=.(.*?).>')
pattern3 = re.compile('id=.expandable_branch_.*?><a title=.(.*?)href=.(.*?).>.*?')
pattern4 =re.compile('.*?href=(.https://my.stu.edu.cn/courses/campus/mod/resource/view.php.*?).>.img.*?/f/(.*?).24.*?instancename.>(.*?)<.*?')



def download_file(url2,pathb):
    r2_file = s.get(url2)
    content2_file = r2_file.text
    position1 = content2_file.find('section-1')
    position2 = content2_file.find('id="region-pre"')
    content2_file =content2_file[position1-200:position2]
    items4 = re.findall(pattern4,content2_file)


    for item_file in items4:               
        
        name = item_file[2].replace('*','_').replace('/','_').replace('\\','_').replace(':','_').replace('?','_').replace('"','_').replace('<','_').replace('>','_').replace('|','_')
        print name  

        if (item_file[1]=='powerpoint'):
            if ((name[-4:]=='.ppt')or(name[-5:]=='.pptx')):                
                name = name
            else:
                name = name + '.ppt'
            print 'check'         
            print name

        if (item_file[1]=='spreadsheet'):
            if ((name[-4:]=='.xls')or(name[-5:]=='.xlsx')):                
                name = name
            else:
                name = name + '.xls'
            print 'check'         
            print name

        if (item_file[1]=='document'):
            if ((name[-4:]=='.doc')or(name[-5:]=='.docx')):                
                name = name
            else:
                name = name + '.doc'
            print 'check'         
            print name

            
        if (item_file[1]=='pdf'):
            if (name[-4:]=='.pdf'):
                name = name
            else:
                name = name + '.pdf'
            print 'check'         
            print name
    
        if (item_file[1]=='jpeg'):
            continue
        if (item_file[1]=='archive'):
            continue
            name = name +'.rar'
        
        new_url = item_file[0][1:]

        filepath= pathb
        path =  filepath + name 
        if (not os.path.exists(path)):
            inword = s.get(new_url)
            with open(path,'wb') as code :
                code.write(inword.content)
            print u'下载成功'
        else :
            print u'文件已经存在'


url = 'https://sso.stu.edu.cn/login'
url3 = 'https://my.stu.edu.cn/courses/campus/my'    

s = requests.Session()
te = s.get(url)
findit = te.text
items = re.findall(pattern,findit)
items2 = re.findall(pattern2,findit)
for item in items:
    lt=item[0:len(item)-2].encode()   
for item in items2:    
    el=item[0:4].encode()
headers={
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
         }
postData={'_eventId': 'submit',
          'execution': el,
          'lt':lt,
          'username':'15ytli3',          
          'password':'Eatin970105'}
s.post(url,data= postData,headers=headers)


r=s.get(url3)

content = r.text

items3 = re.findall(pattern3,content)
for item in items3:
    logn=len(item[0])-2
    item_change = item[0][8:logn].replace('*','_').replace('/','_').replace('\\','_').replace(':','_').replace('?','_').replace('"','_').replace('<','_').replace('>','_').replace('|','_')
    user = postData['username']
    if os.path.exists(('/home/pi/'+user+'/'+item[0][1:7]+'/'+item_change)):
        print u'文件夹存在'
    else :
        print u'正在创建文件夹'
        os.makedirs(('/home/pi/'+user+'/'+item[0][1:7]+'/'+item_change))
           
    pathb =('/home/pi/'+user+'/'+item[0][1:7]+'/'+item_change)+'/'
    print pathb
    url2=item[1]
    print url2

    download_file(url2,pathb)



