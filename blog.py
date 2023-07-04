# -*- coding: utf-8 -*-
import os
import markdown
import argparse
from github import Github
from xpinyin import Pinyin

host_name="https://meekdai.github.io/"

index_md="\r\n#### 文章列表\r\n"

def md2html(title,mdstr):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.toc']
    html = '''
    <html>
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <link href="../static/default.css" rel="stylesheet">
    <link href="../static/github.css" rel="stylesheet">
    </head>
    <body>
    <h1>%s</h1>
    %s
    </body>
    </html>
    '''
    if title=="首页":
        html = '''
        <html>
        <head>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <link href="static/default.css" rel="stylesheet">
        <link href="static/github.css" rel="stylesheet">
        </head>
        <body>
        <h1>%s</h1>
        %s
        </body>
        </html>
        '''
    ret = markdown.markdown(mdstr,extensions=exts)
    return html % (title,ret)

def createHtml(title,body,dir_name):
    global index_md
    genHtml = dir_name+'{}.html'.format(Pinyin().get_pinyin(title))
    f = open(genHtml, 'w', encoding='UTF-8')
    message = md2html(title,body)
    f.write(message)
    f.close()
    index_md=index_md+("- [%s](%s)\r\n" % (title,host_name+genHtml))

def createIndex():
    global index_md
    f = open("index.html", 'w', encoding='UTF-8')
    message = md2html("首页",index_md)
    f.write(message)
    f.close()

def get_repo(user: Github, repo: str):
    return user.get_repo(repo)

def main(token,repo_name,issue_number=None, dir_name=""):
    user = Github(token)
    repo = get_repo(user, repo_name)
    for issue in repo.get_issues():
        createHtml(issue.title,issue.body,dir_name)

    createIndex()


if __name__ == "__main__":
    os.chdir("docs/")
    parser = argparse.ArgumentParser()
    parser.add_argument("github_token", help="github_token")
    parser.add_argument("repo_name", help="repo_name")
    parser.add_argument("--issue_number", help="issue_number", default=None, required=False)
    options = parser.parse_args()

    if not os.path.exists("post/"):
        os.mkdir("post/")

    main(options.github_token, options.repo_name,dir_name="post/")


