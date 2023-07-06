# -*- coding: utf-8 -*-
import os
import requests
import argparse
from github import Github
from xpinyin import Pinyin

######################################################################################
def postmd2html(title,mdstr):
    global options
    global post_html
    global avatarUrl
    global blog_name
    
    payload = {"text": mdstr, "mode": "markdown"}
    ret=requests.post("https://api.github.com/markdown", json=payload,headers={"Authorzation":"token {}".format(options.github_token)})
    if ret.status_code==200:
        return post_html % (title,avatarUrl,options.blog_url,blog_name,title,ret.text)
    else:
        raise Exception("post md2html error title=%s status_code=%d"%(title,ret.status_code))

def createPost(title,body,dir_name):
    global options
    global index_md
    genHtml = dir_name+'{}.html'.format(Pinyin().get_pinyin(title))
    f = open(genHtml, 'w', encoding='UTF-8')
    message = postmd2html(title,body)
    f.write(message)
    f.close()
    index_md=index_md+("- [%s](%s)\r\n" % (title,genHtml))
    print("create title=%s file=%s ok" % (title,genHtml))
######################################################################################
def indexmd2html(mdstr):
    global options
    global index_html
    global avatarUrl
    global blog_name

    payload = {"text": mdstr, "mode": "markdown"}
    ret=requests.post("https://api.github.com/markdown", json=payload,headers={"Authorzation":"token {}".format(options.github_token)})
    if ret.status_code==200:
        return index_html % (blog_name,avatarUrl,options.blog_url,blog_name,ret.text)
    else:
        raise Exception("index md2html error title=%s status_code=%d"%(title,ret.status_code))

def createIndex():
    global index_md
    f = open("index.html", 'w', encoding='UTF-8')
    message = indexmd2html(index_md)
    f.write(message)
    f.close()
    print("create index.html ok")

######################################################################################
def get_repo(user: Github, repo: str):
    return user.get_repo(repo)

def main(token,repo_name,issue_number=None, dir_name=""):
    global avatarUrl
    global blog_name
    user = Github(token)
    repo = get_repo(user, repo_name)
    avatarUrl=user.get_user().avatar_url
    blog_name=user.get_user().login

    print("====== start create static html ======")
    for issue in repo.get_issues():
        createPost(issue.title,issue.body,dir_name)
        
    createIndex()
    print("====== create static html end ======")


if __name__ == "__main__":
    global options
    global index_md
    global index_html
    global post_html
    index_md = "\r\n#### 文章列表\r\n"
    index_html=open('index_example.html', 'r', encoding='utf-8').read()
    post_html=open('post_example.html', 'r', encoding='utf-8').read()
    
    os.chdir("docs/")
    parser = argparse.ArgumentParser()
    parser.add_argument("github_token", help="github_token")
    parser.add_argument("repo_name", help="repo_name")
    parser.add_argument("blog_url", help="blog_url")
    parser.add_argument("--issue_number", help="issue_number", default=None, required=False)
    options = parser.parse_args()

    if not os.path.exists("post/"):
        os.mkdir("post/")

    main(options.github_token, options.repo_name,dir_name="post/")


