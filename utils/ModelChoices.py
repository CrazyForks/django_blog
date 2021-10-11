

# https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/#enumeration-types


# 单独提取出来是因为到时候 views 里 也 会用到

from django.db import models

class ChoicesArticleStatus(models.IntegerChoices):
    DRAFT = -1, '草稿'
    PUBLIC = 1, '公开'
    PRIVATE = 0, '隐藏'
