
# markdown start
from urllib.parse import urlparse

import markdown





from ._markdown_plugins import BootStrap_table_Extension

def md2html(mdstr):
    # 官方插件 https://python-markdown.github.io/extensions/
    # 第三方插件 https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions
    exts = ['markdown.extensions.extra',
            # 'codehilite',  # 代码块（高亮）
            'nl2br',  # 回车强制换行，模仿github的markdown
            # BootStrap_table_Extension(),  # 为了支持表格 table,

            # 'markdown.extensions.tables', # 为了支持表格 table
            # 'markdown.extensions.toc',
            ]
    ret = markdown.markdown(mdstr,extensions=exts)
    return  ret






# markdown end




import bleach  # markdown特殊字符

# 有bug，代码块也会把网址添加a标签
# 自定义功能，给链接添加属性
def set_attrs_my(attrs, new=False):
    full_url = urlparse(attrs[(None, 'href')])
    if full_url.netloc not in ['piqizhu.com', 'www.piqizhu.com', '']: # 如果不是站内链接，就要添加nofollow
        attrs[(None, 're')] = 'nofollow'
    attrs[(None, 'target')] = '_blank'
    return attrs
linker_my = bleach.linkifier.Linker(callbacks=[set_attrs_my], skip_tags=["code",])



def html_clean(htmlstr):
    """
    采用bleach来清除不必要的标签，并linkify text
    """

    # 允许的标签
    markdown_tags = [
        "h1", "h2", "h3", "h4", "h5", "h6",
        "b", "i", "strong", "em", "tt",
        "p", "br",
        "span", "div", "blockquote", "code", "hr",
        "ul", "ol", "li", "dd", "dt",
        "img",
        "a",
        "sub", "sup", "pre",
        "table", "thead", "tr", "th", "td", "tbody",
    ]
    # 允许的属性
    markdown_attrs = {
        "*": ["id","class"],
        "img": ["src", "alt", "title"],
        "a": ["href", "alt", "title", "target", "rel"],
    }


    tmp= bleach.clean(htmlstr, tags=markdown_tags, attributes=markdown_attrs) # 标签过滤
    tmp = linker_my.linkify(tmp) # 网址变成超链接，并添加 rel="nofollow"


    return tmp
    # return tmp

def md2html_and_html_clean(mdstr):
    return html_clean(md2html(mdstr))
