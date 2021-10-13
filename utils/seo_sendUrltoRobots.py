# seo优化，发送网址给 搜索引擎


from django.contrib.sitemaps import ping_google
from django.conf import settings
from urllib import request, parse



def sendToGoogle():
    try:
        ping_google()
    except Exception:
        # 考虑到国内无法访问google，加个容错，以免引起程序错误
        pass


def sendToBaidu(url):
    百度推送接口 = settings.SEO.get("百度推送接口", None)

    if 百度推送接口 is None:
        raise ValueError("获取 百度 推送接口出错了~~~")

    # 从推送接口，提取site
    site = dict(parse.parse_qsl(parse.urlsplit(百度推送接口).query))
    site = site.get("site", None)

    if site is None:
        raise ValueError("从百度推送接口中 获取 site 出错了~~~")

    url = site + url  # 拼接url

    req = request.Request(百度推送接口,method="POST", data=url.encode('utf-8'))
    response = request.urlopen(req)

    res = str(response.read())

    if url not in res:
        print(f"推送url:{url} 到百度搜索 成功")
    else:
        print(f"推送url:{url} 到百度搜索 失败了~~~")



def sendToSEO(url):
    sendToBaidu(url)
    sendToGoogle()
