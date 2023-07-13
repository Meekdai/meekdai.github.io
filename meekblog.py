# -*- coding: utf-8 -*-
import os
import requests
import argparse
from github import Github
from xpinyin import Pinyin
######################################################################################
class MEEKBLOG():
    def __init__(self,options,post_dir,backupMd=False):
        self.options=options
        self.post_dir=post_dir
        self.index_example=open('index_example.html', 'r', encoding='utf-8').read()
        self.post_example=open('post_example.html', 'r', encoding='utf-8').read()
        self.index_md=''
        self.post_year=0
        self.header_right=''
        self.backupMd=backupMd

        user = Github(self.options.github_token)
        self.repo = self.get_repo(user, options.repo_name)
        self.avatar_url=user.get_user().avatar_url
        self.blog_name=user.get_user().login

        self.checkPostDir()

    def checkPostDir(self):
        os.chdir("docs/")
        if not os.path.exists(self.post_dir):
            os.mkdir(self.post_dir)
        if self.backupMd:
            if not os.path.exists("backup/"):
                os.mkdir("backup/")

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
            gen_Html = self.post_dir+'{}.html'.format(Pinyin().get_pinyin(issue.title))
        else:
            gen_Html = single+".html"
        f = open(gen_Html, 'w', encoding='UTF-8')
        post_body=self.markdown2html(issue.body)
        source_url="https://github.com/"+options.repo_name+"/issues/"+str(issue.number)
        f.write(self.value2postHtml(self.blog_name,issue.title,post_body,self.avatar_url,source_url,self.header_right))
        f.close()

        if self.backupMd:
            f = open("backup/"+issue.title+".md", 'w', encoding='UTF-8')
            f.write(issue.body)
            f.close()
        return gen_Html

    def value2postHtml(self,blog_name,post_title,post_body,avatar_url,source_url,header_right):
        return self.post_example%(post_title,avatar_url,blog_name,header_right,post_title,source_url,post_body)

    def creatIndexHtml(self):
        f = open("index.html", 'w', encoding='UTF-8')
        index_body=self.markdown2html(self.index_md)
        f.write(self.value2indexHtml(self.blog_name,index_body,self.avatar_url,self.header_right))
        f.close()

    def value2indexHtml(self,blog_name,index_body,avatar_url,header_right):
        return self.index_example%(blog_name,avatar_url,blog_name,header_right,index_body)

    def runAll(self):
        print("====== start create static html ======")
        issues=self.repo.get_issues()

        for issue in issues:
            for label in issue.labels:
                if label.name!='post':
                    self.header_right=self.header_right+('<div class="Header-item"><a href="/%s.html" class="Header-link">%s</a></div>' % (label.name,issue.title))

        for issue in issues:
            for label in issue.labels:
                if label.name=='post':
                    gen_Html=self.createPostHtml(issue)
                    if self.post_year!=issue.created_at.year:
                        self.post_year=issue.created_at.year
                        self.index_md=self.index_md+("## %s \r\n"%self.post_year)
                    self.index_md=self.index_md+("- %s &nbsp;&nbsp;&nbsp;&nbsp;[%s](%s)\r\n" % (issue.created_at.strftime("%Y-%m-%d"),issue.title,gen_Html))
                    print("create postPage title=%s file=%s " % (issue.title,gen_Html))

                else:
                    gen_Html=self.createPostHtml(issue,single=label.name)
                    print("create singlePage title=%s file=%s ok" % (issue.title,gen_Html))
                    
                    

        self.creatIndexHtml()
        print("create index.html")
        print("====== create static html end ======")

######################################################################################

parser = argparse.ArgumentParser()
parser.add_argument("github_token", help="github_token")
parser.add_argument("repo_name", help="repo_name")
parser.add_argument("--issue_number", help="issue_number", default=0, required=False)
options = parser.parse_args()
blog=MEEKBLOG(options,'post/')
blog.runAll()

######################################################################################