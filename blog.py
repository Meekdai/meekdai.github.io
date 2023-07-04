# -*- coding: utf-8 -*-
import markdown
import argparse
from github import Github
from xpinyin import Pinyin
py=Pinyin()

# g = Github("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")
# repo=g.get_user().get_repos()[10]




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
    ret = markdown.markdown(mdstr,extensions=exts)
    return html % (title,ret)

def saveHtml(title,body,dir_name):
    genHtml = dir_name+'/post/{}.html'.format(py.get_pinyin(title))
    f = open(genHtml, 'w', encoding='UTF-8')
    message = md2html(title,body)
    f.write(message)
    f.close()

def main(token,repo_name,issue_number=None, dir_name="docs"):
    user = Github(token)
    repo= user.get_user().get_repo(repo_name)
    for issue in repo.get_issues():
        saveHtml(issue.title,issue.body,dir_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("github_token", help="github_token")
    parser.add_argument("repo_name", help="repo_name")
    options = parser.parse_args()
    main(options.github_token, options.repo_name)
