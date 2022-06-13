#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: 文件.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 文件 的自动化操作
#############################################
from MainTypes.FileType import MainFile
from MainTypes.SearchByContentType import MainSearchByContent

mainFile = MainFile()
mainSearchByContent = MainSearchByContent()


def replace4filename(path, del_content, replace_content=None):
    mainFile.replace4filename(path, del_content, replace_content)


def search_by_content(search_path, content):  # 定义 search() 函数，传入 "path" 文件路径， "target" 要查找的目标文件
    mainSearchByContent.search_by_content(search_path, content)
