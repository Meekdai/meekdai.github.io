#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://pygithub.readthedocs.io/en/stable/examples/Issue.html
from github import Github
g = Github("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")
repo=g.get_user().get_repos()[10]

import markdown
from xpinyin import Pinyin
py=Pinyin()

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

def saveHtml(title,body):
    genHtml = 'docs/post/{}.html'.format(py.get_pinyin(title))
    f = open(genHtml, 'w', encoding='UTF-8')
    message = md2html(title,body)
    f.write(message)
    f.close()

def savePost(id):
    saveHtml(repo.get_issues()[id].title,repo.get_issues()[id].body)

savePost(0)
savePost(1)
savePost(2)
