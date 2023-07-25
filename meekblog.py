# -*- coding: utf-8 -*-
import os
import json
import time
import datetime
import shutil
import requests
import argparse
from github import Github
from xpinyin import Pinyin
######################################################################################
avatar_url="http://meekdai.com/avatar.jpg"

######################################################################################
class MEEKBLOG():
    def __init__(self,options,post_dir):
        self.options=options
        self.post_dir=post_dir
        self.index_example=open('index_example.html', 'r', encoding='utf-8').read()
        self.post_example=open('post_example.html', 'r', encoding='utf-8').read()
        self.index_md=''
        self.post_year=0
        self.header_right=''

        self.postDict=json.loads('{}')

        user = Github(self.options.github_token)
        self.repo = self.get_repo(user, options.repo_name)
        # self.avatar_url=user.get_user().avatar_url
        self.avatar_url=avatar_url
        self.blog_name=user.get_user().login

    def cleanFile(self):
        if os.path.exists("backup/"):
            shutil.rmtree("backup/")
            
        if os.path.exists("docs/"):
            shutil.rmtree("docs/")

        os.mkdir("backup/")
        os.mkdir("docs/")
        os.mkdir(self.post_dir)
        

    def get_repo(self,user: Github, repo: str):
        return user.get_repo(repo)

    def markdown2html(self,mdstr):
        payload = {"text": mdstr, "mode": "markdown"}
        ret=requests.post("https://api.github.com/markdown", json=payload,headers={"Authorzation":"token {}".format(self.options.github_token)})
        if ret.status_code==200:
            return ret.text
        else:
            raise Exception("markdown2html error status_code=%d"%(ret.status_code))

    def createPostHtml(self,issue,single=None):
        if single==None:
            gen_Html = self.post_dir+'{}.html'.format(Pinyin().get_pinyin(issue["title"]))
        else:
            gen_Html = "docs/"+single+".html"
        
        f = open("backup/"+issue["title"]+".md", 'r', encoding='UTF-8')
        post_body=self.markdown2html(f.read())
        f.close()

        f = open(gen_Html, 'w', encoding='UTF-8')
        f.write(self.value2postHtml(self.blog_name,issue["title"],post_body,self.avatar_url,issue["source_url"],self.header_right))
        f.close()

        return gen_Html

    def value2postHtml(self,blog_name,post_title,post_body,avatar_url,source_url,header_right):
        return self.post_example%(post_title,avatar_url,blog_name,header_right,post_title,source_url,post_body)

    def creatIndexHtml(self):
        self.postDict=dict(sorted(self.postDict.items(),key=lambda x:x[1]["created_at"],reverse=True))#使列表由时间排序
        for num in self.postDict:
            if self.postDict[num]["label"]=='post':
                post_time = datetime.datetime.fromtimestamp(self.postDict[num]["created_at"])
                if self.post_year!=post_time.year:
                    self.post_year=post_time.year
                    self.index_md=self.index_md+("## %s \r\n"%(self.post_year))
                self.post_url=self.post_dir[5:]+'{}.html'.format(Pinyin().get_pinyin(self.postDict[num]["title"]))
                self.index_md=self.index_md+("- %s &nbsp;&nbsp;&nbsp;&nbsp;[%s](%s)\r\n" % (post_time.strftime("%Y-%m-%d"),self.postDict[num]["title"],self.post_url))
            else:
                self.header_right=self.header_right+('<div class="Header-item"><a href="/%s.html" class="Header-link">%s</a></div>' % (self.postDict[num]["label"],self.postDict[num]["title"]))

        f = open("docs/index.html", 'w', encoding='UTF-8')
        index_body=self.markdown2html(self.index_md)
        f.write(self.value2indexHtml(self.blog_name,index_body,self.avatar_url,self.header_right))
        f.close()
        print("create docs/index.html")

    def value2indexHtml(self,blog_name,index_body,avatar_url,header_right):
        return self.index_example%(blog_name,avatar_url,blog_name,header_right,index_body)

    def addOnePostJson(self,issue):
        for label in issue.labels:
            self.postDict[issue.number]=json.loads('{}')
            self.postDict[issue.number]["label"]=label.name
            self.postDict[issue.number]["title"]=issue.title
            self.postDict[issue.number]["source_url"]="https://github.com/"+options.repo_name+"/issues/"+str(issue.number)
            try:
                modifyTime=json.loads(issue.body.split("\r\n")[-1:][0].split("##")[1])
                self.postDict[issue.number]["created_at"]=modifyTime["timestamp"]
            except:
                self.postDict[issue.number]["created_at"]=int(time.mktime(issue.created_at.timetuple()))
        f = open("backup/"+issue.title+".md", 'w', encoding='UTF-8')
        f.write(issue.body)
        f.close()

    def creatOneHtml(self,issue):
        if issue["label"]=='post':
            gen_Html=self.createPostHtml(issue)
            print("create postPage title=%s file=%s " % (issue["title"],gen_Html))
        else:
            gen_Html=self.createPostHtml(issue,single=issue["label"])
            print("create singlePage title=%s file=%s ok" % (issue["title"],gen_Html))

    def runAll(self):
        print("====== start create static html ======")
        self.cleanFile()

        issues=self.repo.get_issues()
        for issue in issues:
            self.addOnePostJson(issue)

        for num in self.postDict:
            self.creatOneHtml(self.postDict[num])

        self.creatIndexHtml()
        print("====== create static html end ======")

    def runOne(self,number):
        print("====== start create static html ======")
        issue=self.repo.get_issue(int(number))
        self.addOnePostJson(issue)
        self.creatOneHtml(self.postDict[number])
        self.creatIndexHtml()
        print("====== create static html end ======")

######################################################################################

parser = argparse.ArgumentParser()
parser.add_argument("github_token", help="github_token")
parser.add_argument("repo_name", help="repo_name")
parser.add_argument("--issue_number", help="issue_number", default=0, required=False)
options = parser.parse_args()

blog=MEEKBLOG(options,'docs/post/')

if not os.path.exists("postList.json"):
    print("postList is not exists, runAll")
    blog.runAll()
else:
    if options.issue_number=="0" or options.issue_number=="":
        print("issue_number=='0', runAll")
        blog.runAll()
    else:
        f=open("postList.json","r")
        print("postList is exists and issue_number!=0, runOne")
        blog.postDict=json.loads(f.read())
        f.close()
        blog.runOne(options.issue_number)

listFile=open("postList.json","w")
listFile.write(json.dumps(blog.postDict))
listFile.close()


######################################################################################