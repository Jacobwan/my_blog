#coding=utf-8
from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.tag_name
        
class Article(models.Model):
    title = models.CharField(max_length = 100)#博客题目
    category = models.CharField(max_length = 50, blank = True)#博客分类 可为空
    tag = models.ManyToManyField(Tag, blank=True)  # 博客标签 可为空
    date_time = models.DateTimeField(auto_now_add = True)#博客日期
    content = models.TextField(blank = True, null = True)#博客正文

    def __unicode__(self):
        return self.title

    class Meta:   #按时间下降排序
        ordering = ['-date_time']



