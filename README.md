
项目状态： 正在开发中【目前已基本可用】

项目地址： https://github.com/find456789/django_blog

# django_blog
django+bootstrap5 实现的 个人博客






# 特点

### 后台
- [x] 后台 文章、分类 的增删改查
- [x] 后台 文章 使用markdown格式保存
- [x] 后台 文章的历史版本管理（类似git，可随时回退到任何历史版本）
- [x] 后台 新建文章 自动推送到百度、谷歌搜索引擎
- [ ] 图床
- [ ] 后台 编辑器 支持粘贴上传图片
- [ ] 网站出现异常、崩溃 发送邮件

### 前台
- [x] 前台 文章 查看、搜索
- [x] 前台 文章 代码高亮
- [x] rss、atom、sitemap
- [ ] 评论功能
- [ ] 文章页面的toc 导航





# 如何运行演示项目

- 克隆到本地
- `pip install -r requirements.txt`
- `python manage.py runserver`
- 打开 `http://127.0.0.1:8000/` 就可以了

后台地址：  http://127.0.0.1:8000/admin/

账号：admin888

密码：admin888

# 如何使用
- 克隆到本地
- `pip install -r requirements.txt`
- 删除旧的测试数据库 `db.sqlite3`
- 把配置文件 `django_blog/django_blog/settings.py` 最底部的 `DEBUG = True` 改为 `DEBUG = False`
- 执行 `python manage.py migrate` 创建数据库
- 执行 `python manage.py createsuperuser` 根据步骤创建超级管理员账号
- 执行 `python manage.py runserver` 启动服务
- 打开 `http://127.0.0.1:8000/` 就可以了

# 截图展示
## 源码-配置信息
![image](https://user-images.githubusercontent.com/6580897/136949249-a0caf031-d7c9-4264-a889-8bc177970249.png)


## 前台-首页
![image](https://user-images.githubusercontent.com/6580897/136948957-f1b939c5-765a-45a9-98ed-ec51546601cd.png)

## 前台-文章列表页
![image](https://user-images.githubusercontent.com/6580897/137469358-c1b760a9-29f9-4a39-bc5a-781e70fcc265.png)

## 前台-文章详情页
![image](https://user-images.githubusercontent.com/6580897/137469418-dabf8fc7-65bf-4d22-80fe-3e8d97717135.png)

## 前台-关于我
![image](https://user-images.githubusercontent.com/6580897/136949027-be794446-a04b-47cc-86e6-433bf5c58a2a.png)

## 后台-首页
![image](https://user-images.githubusercontent.com/6580897/136937552-3a825fef-4136-44e7-afef-133d9916d2d3.png)

## 后台-分类管理
![image](https://user-images.githubusercontent.com/6580897/136937582-b3149c74-b4ae-4336-a358-dacd711c82ea.png)

## 后台-文章列表管理
![image](https://user-images.githubusercontent.com/6580897/136937619-0e27e2ba-b74b-4461-9dfd-267ec2b511ae.png)

## 后台-文章详情管理
![image](https://user-images.githubusercontent.com/6580897/136937652-3c955e7f-1ff4-494d-b143-de38cedfaac7.png)

## 后台-文章历史版本管理
![image](https://user-images.githubusercontent.com/6580897/136937681-32851ab6-e128-4f95-9453-e6fde76e0b4c.png)



# 致谢

https://fontawesome.com/start 图标

https://getbootstrap.com/  ui框架

https://www.djangoproject.com/ django web框架

https://github.com/jazzband/django-debug-toolbar   调试

https://github.com/etianen/django-reversion    admin 版本控制

https://github.com/Python-Markdown/markdown  markdown

https://github.com/mozilla/bleach   过滤非法字符

https://prismjs.com/ 代码高亮

https://staticfile.org/ 部分静态资源托管
