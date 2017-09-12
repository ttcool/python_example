# -*- coding: utf8 -*-
import urllib2,re
from bs4 import BeautifulSoup

allExtLinks = set()
allIntLinks = set()

# 获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # 找出所有以"/"开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getAllExternalLinks(siteUrl):
    req = urllib2.Request(siteUrl)
    html = urllib2.urlopen(req).read()
    bsObj = BeautifulSoup(html, "lxml")
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
            #getAllExternalLinks(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取链接的URL是：" + link)
            allIntLinks.add(link)
            #getAllExternalLinks(link)

getAllExternalLinks("http://oreilly.com")
