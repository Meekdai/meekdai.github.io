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

######################################################################################
class MEEKBLOG():
    def __init__(self,options):
        self.options=options

        self.root_dir='docs/'
        self.post_folder='post/'
        self.post_dir=self.root_dir+self.post_folder

        # self.index_example=open('index_example.html', 'r', encoding='utf-8').read()
        self.plist_example=open('plist_example.html', 'r', encoding='utf-8').read()
        self.post_example=open('post_example.html', 'r', encoding='utf-8').read()

        user = Github(self.options.github_token)
        self.repo = self.get_repo(user, options.repo_name)
        # self.avatar_url=user.get_user().avatar_url
        # self.blog_name=user.get_user().login
        self.labelColorDict=json.loads('{}')
        self.yearColorList=['#bc4c00', '#0969da', '#1f883d', '#A333D0']
        for label in self.repo.get_labels():
            self.labelColorDict[label.name]='#'+label.color

        print(self.labelColorDict)

        self.blogBase=json.loads('{}')
        self.blogBase["title"]=user.get_user().login
        self.blogBase["subTitle"]="童话是一种生活态度，仅此而已。"
        self.blogBase["homeUrl"]="http://meekdai.com"
        self.blogBase["avatarUrl"]="http://meekdai.com/avatar.jpg"
        self.blogBase["filingNum"]="浙ICP备20023628号"
        self.blogBase["singlePage"]=["index","link","about"]
        self.blogBase["postListJson"]=json.loads('{}')

    def cleanFile(self):
        if os.path.exists("backup/"):
            shutil.rmtree("backup/")
            
        if os.path.exists(self.post_dir):
            shutil.rmtree(self.post_dir)

        os.mkdir("backup/")
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

    def createPostHtml(self,issue):
        if issue["label"] in self.blogBase["singlePage"]:
            gen_Html = 'docs/{}.html'.format(issue["label"])
        else:
            gen_Html = self.post_dir+'{}.html'.format(Pinyin().get_pinyin(issue["postTitle"]))

        f = open("backup/"+issue["postTitle"]+".md", 'r', encoding='UTF-8')
        post_body=self.markdown2html(f.read())
        f.close()

        postBase=json.loads('{}')
        postBase["postTitle"]=issue["postTitle"]
        postBase["postBody"]=post_body
        postBase["title"]=self.blogBase["title"]
        postBase["homeUrl"]=self.blogBase["homeUrl"]
        postBase["postSourceUrl"]=issue["postSourceUrl"]

        f = open(gen_Html, 'w', encoding='UTF-8')
        f.write(self.post_example % json.dumps(postBase))
        f.close()
        print("create postPage title=%s file=%s " % (issue["postTitle"],gen_Html))

    def creatPlistHtml(self):
        self.blogBase["postListJson"]=dict(sorted(self.blogBase["postListJson"].items(),key=lambda x:x[1]["createdAt"],reverse=True))#使列表由时间排序

        f = open(self.root_dir+"index.html", 'w', encoding='UTF-8')
        f.write(self.plist_example % json.dumps(self.blogBase))
        f.close()
        print("create docs/index.html")

    def addOnePostJson(self,issue):
        if len(issue.labels)==1:
            postNum="P"+str(issue.number)
            self.blogBase["postListJson"][postNum]=json.loads('{}')
            self.blogBase["postListJson"][postNum]["label"]=issue.labels[0].name
            self.blogBase["postListJson"][postNum]["labelColor"]=self.labelColorDict[issue.labels[0].name]
            self.blogBase["postListJson"][postNum]["postTitle"]=issue.title
            self.blogBase["postListJson"][postNum]["postUrl"]=self.post_folder+'{}.html'.format(Pinyin().get_pinyin(issue.title))
            self.blogBase["postListJson"][postNum]["postSourceUrl"]="https://github.com/"+options.repo_name+"/issues/"+str(issue.number)
            
            try:
                modifyTime=json.loads(issue.body.split("\r\n")[-1:][0].split("##")[1])
                self.blogBase["postListJson"][postNum]["createdAt"]=modifyTime["timestamp"]
            except:
                self.blogBase["postListJson"][postNum]["createdAt"]=int(time.mktime(issue.created_at.timetuple()))

            thisYear=datetime.datetime.fromtimestamp(self.blogBase["postListJson"][postNum]["createdAt"]).year
            self.blogBase["postListJson"][postNum]["dateLabelColor"]=self.yearColorList[int(thisYear)%len(self.yearColorList)]

            f = open("backup/"+issue.title+".md", 'w', encoding='UTF-8')
            f.write(issue.body)
            f.close()

    def runAll(self):
        print("====== start create static html ======")
        self.cleanFile()

        issues=self.repo.get_issues()
        for issue in issues:
            self.addOnePostJson(issue)

        for issue in self.blogBase["postListJson"].values():
            self.createPostHtml(issue)

        self.creatPlistHtml()
        print("====== create static html end ======")

    def runOne(self,number_str):
        print("====== start create static html ======")
        issue=self.repo.get_issue(int(number_str))
        self.addOnePostJson(issue)
        self.createPostHtml(self.blogBase["postListJson"]["P"+number_str])
        self.creatPlistHtml()
        print("====== create static html end ======")

######################################################################################

parser = argparse.ArgumentParser()
parser.add_argument("github_token", help="github_token")
parser.add_argument("repo_name", help="repo_name")
parser.add_argument("--issue_number", help="issue_number", default=0, required=False)
options = parser.parse_args()

blog=MEEKBLOG(options)

if not os.path.exists("blogBase.json"):
    print("blogBase is not exists, runAll")
    blog.runAll()
else:
    if options.issue_number=="0" or options.issue_number=="":
        print("issue_number=='0', runAll")
        blog.runAll()
    else:
        f=open("blogBase.json","r")
        print("blogBase is exists and issue_number!=0, runOne")
        blog.blogBase=json.loads(f.read())
        f.close()
        blog.runOne(options.issue_number)

listFile=open("blogBase.json","w")
listFile.write(json.dumps(blog.blogBase))
listFile.close()


######################################################################################