#!/usr/bin/python
# -*- coding: utf-8 -*-

from github import Github
from github.Issue import Issue
from github.Repository import Repository
import os
import time
import urllib.parse
import codecs

user: Github
username: str
ghiblog: Repository

def update_readme_md_file(contents):
    with codecs.open('README.md', 'w', encoding='utf-8') as f:
        f.writelines(contents)
        f.flush()
        f.close()


def login():
    global user, username
    github_repo_env = os.environ.get('GITHUB_REPOSITORY')
    username = github_repo_env[0:github_repo_env.index('/')]
    password = os.environ.get('GITHUB_TOKEN')
    user = Github(username, password)


def get_ghiblog():
    global ghiblog
    ghiblog = user.get_repo(os.environ.get('GITHUB_REPOSITORY'))


def bundle_new_created_section():
    global ghiblog

    new_5_created_issues = ghiblog.get_issues()[:5]

    new_created_section = '## 最新 :new: \n'

    for issue in new_5_created_issues:
        print(issue)
        # new_created_section += format_issue_with_labels(issue)

    return new_created_section

def execute():
    login()
    get_ghiblog()
    new_created_section = bundle_new_created_section()

    # update_readme_md_file(contents)


if __name__ == '__main__':
    execute()
