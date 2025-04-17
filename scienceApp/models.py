from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class Direction(models.Model):
    """研究方向模型"""
    name = models.CharField('方向名称', max_length=100)
    slug = models.SlugField('URL别名', max_length=100, unique=True)
    description = models.TextField('方向描述', blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    
    class Meta:
        verbose_name = '研究方向'
        verbose_name_plural = '研究方向'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('science:direction_detail', args=[self.slug])


class Research(models.Model):
    """科研成果模型"""
    title = models.CharField('标题', max_length=200)
    slug = models.SlugField('URL别名', max_length=200, unique=True)
    direction = models.ForeignKey(
        Direction, 
        on_delete=models.CASCADE,
        related_name='researches',
        verbose_name='研究方向'
    )
    content = RichTextUploadingField('内容')
    summary = models.TextField('摘要', blank=True)
    publish_date = models.DateField('发布日期', default=timezone.now)
    is_featured = models.BooleanField('是否推荐', default=False)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    
    # 封面图片
    cover_image = models.ImageField('封面图片', upload_to='research_covers/', blank=True, null=True)
    
    # 科研成果核心点
    core_feature_1 = models.CharField('核心特点1', max_length=100, blank=True)
    core_feature_2 = models.CharField('核心特点2', max_length=100, blank=True)
    core_feature_3 = models.CharField('核心特点3', max_length=100, blank=True)
    
    class Meta:
        verbose_name = '科研成果'
        verbose_name_plural = '科研成果'
        ordering = ['-publish_date']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('science:research_detail', args=[self.slug])


class Member(models.Model):
    """团队成员模型"""
    name = models.CharField('姓名', max_length=100)
    position = models.CharField('职位', max_length=100)
    bio = models.TextField('简介')
    avatar = models.ImageField('头像', upload_to='member_avatars/')
    email = models.EmailField('邮箱', blank=True)
    is_key_member = models.BooleanField('是否核心成员', default=False)
    order = models.IntegerField('排序', default=0)
    
    class Meta:
        verbose_name = '团队成员'
        verbose_name_plural = '团队成员'
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name