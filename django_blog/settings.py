"""
Django settings for django_blog project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eaaltcixk533#1!5l91#4oo@dr4_)@lfqbp3mbj3z$b#7p!gy#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#########################################################################
#########################################################################
#################上方是django默认配置，不做任何修改###########################
#################在下方覆盖默认配置，方便以后做迁移############################
#########################################################################
#########################################################################

# 是否开启调试模式
DEBUG = True

# 中文界面
LANGUAGE_CODE = 'zh-hans'

# 时区改成北京时间
TIME_ZONE = 'Asia/Shanghai'

# 正式环境，允许哪些host(域名、ip)访问
ALLOWED_HOSTS = ['127.0.0.1', 'xxx.com']

# 要启用的app
INSTALLED_APPS += [
    'django.contrib.sitemaps',
    'reversion',
    'blog'
]

# seo 每次新建文章后，推送网址到搜索引擎
SEO = {
    "开启": False,  # 为True则开启每次新建文章就推送，开启前必须正确配置，否则运行会出错

    # 百度推送接口从这里获取  https://ziyuan.baidu.com/linksubmit/index ,你需要先把你的网站添加到【百度站长】
    "百度推送接口": "http://data.zz.baidu.com/urls?site=https://xxxx.com&token=Xxxxxx22",  # 若开启，那这里必须填写正确
    # 谷歌推送接口不用做配置，但要求你去这里添加你的站点 https://search.google.com/search-console/welcome
    "谷歌": ""
}

# 网站上很多信息的配置
SITE_CONFIG = {
    "网站名称": "王大锤的技术博客",
    "网站描述": "分享一些编程技术文章。。。",

    # 要控制、扩展 我的信息，可修改 模板： templates/user_info.html
    "我的信息": {
        "头像": "https://gdown.baidu.com/img/0/200_200/1c7d0637ca01803040e087fb44e47654.png", # 可输入网址，也可以输入base64
        "名字": "王大锤",
        "地址": "银河系太阳系地月系地球亚洲中国xx省xx市xx区xxxxx号xxx",  # 不想显示就改成 None
        "座右铭": "大王叫我来巡山~~~~呐~~~", # 仅支持纯文本，暂不支持html、markdown

        "社交信息":  {
            "github": {
                "显示": True,  # 若为True，前台就会显示
                "内容": "https://github.com/find456789/django_blog",  # 这里记得改成你自己的github网址
            },
            "微博": {
                "显示": True,  # 若为True，前台就会显示
                "内容": "https://weibo.com/xxx",  # 如 https://weibo.com/xxx
            },

            "微信": {
                "显示": True,  # 若为True，前台就会显示
                "内容": "https://gdown.baidu.com/img/0/200_200/1c7d0637ca01803040e087fb44e47654.png",  # 可输入网址，也可以输入base64
            },

            "微信公众号": {
                "显示": True,  # 若为True，前台就会显示
                "内容": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADgAAAA4CAMAAACfWMssAAAAbFBMVEUAAAD//////1X//2b/41X/6lX/51D/4lL/41D/41D/4k3/403/4k7/4U7/4k//4U7/4U3/4U7/4U3/4k7/4k7/4k7/4U7/4U7/4k3/4U7/4k7/4U7/4U5cOSVsSimpiDeujTnFpT/83Uz/4U2D8A1lAAAAHXRSTlMAAQMFCQwgNTZJT2NyeYWam6ussMLS1d/k6ezw+ZtQLqkAAAFWSURBVEjHpZfbsoIwDEVjUUEoF+VqoXBw//8/ngfUUS6ljeuxM8vJ0DTZEq0gfJkWteo6VRep9AVZ4YXXFl+019Db1Y6xwgoqPho1ETXYoIkMFV8qGKguG9ohwQ7JYc075dglPy29cwkLyvPCu8OK+8w8lbCk/Kr2kMOa/PMLJXAg+bg/OPG+T1G5idWrhyI4Ej37unEVm6njYzgTExF5yl1UHhGFYBAS0Y0jXonEbE48hr4fHuYToBUUzH5r0FrrwXwCwCc5O+m11ro3nwCQlPHEjApeqQXV4Hwc1KTAQlHHEzu+yC615on14josKRYNYEm6aDlLJPk80V88KztasfWQx78n49ZDXh8do34zbo2O1WG1IypvczyaS41/G8jsFcBfOuw1x1+s/FXODg/8uMIPSPxIxg+B/Nj5Q9DlR+spzN/mYf5mEeanigOZvf4+ZDJYrfEfMjVK7C1/36oAAAAASUVORK5CYII=",  # 可输入网址，也可以输入base64
            },
            "rss": {
                # rss的地址django会自动处理，你可以控制是否显示
                "显示": True,  # 若为True，前台就会显示
            },
        }

    },





}



# 如果开启了调试，那么就要加载这些配置
if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    INTERNAL_IPS = ["127.0.0.1", ]
