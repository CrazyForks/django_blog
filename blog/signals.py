# 信号
from utils.seo_sendUrltoRobots import sendToSEO
from django.conf import settings

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import Article, Category, category_haveNo


@receiver(post_delete, sender=Category, dispatch_uid='Category-post_delete')
def when_Category_delete(sender, instance, **kwargs):
    # 分类被删后，文章就会自动到 未分类下， 所以，需要更新 未分类 的 article_count
    category_haveNo().update_article_count()


@receiver(post_delete, sender=Article, dispatch_uid='Article-post_delete')
def when_Article_delete(sender, instance, **kwargs):
    instance.category.update_article_count()  # 文章被删后，更新分类信息里的 article_count


@receiver(post_save, sender=Article, dispatch_uid='Article-post_save')
def when_Article_save(sender, instance, created, **kwargs):
    if created:
        instance.category.update_article_count()  # 更新分类信息

        # 如果开启了seo： 每次新建文章 就推送，那就执行响应代码
        if settings.SEO.get("启用", None):
            sendToSEO(instance.get_absolute_url())

    else:
        # 虽然更新文章 不需要更新 分类下的 article_count字段，但
        # 但如果是从删除的记录里恢复记录，就会触发 更新，也就是会执行这个分支的代码，所以，需要再这里 更新分类信息
        instance.category.update_article_count()  # 更新分类信息
