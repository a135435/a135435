# 制造科学应用

制造科学应用是一个基于Django开发的科研成果展示平台，为科研机构提供成果发布、展示和管理功能。

## 主要功能

- 科研成果发布与展示
- 研究方向分类管理
- 科研团队成员展示
- 响应式设计，适配多种设备
- 富文本编辑，支持图文混排

## 技术栈

- Django 4.2.4
- Python 3.8+
- PostgreSQL (生产环境)
- SQLite (开发环境)
- Bootstrap 5
- CKEditor 富文本编辑器
- AWS S3 (可选，用于媒体文件存储)

## 安装与使用

1. 克隆仓库

```bash
git clone https://github.com/yourusername/scienceapp.git
cd scienceapp
```

2. 创建虚拟环境并安装依赖

```bash
python -m venv venv
source venv/bin/activate  # Windows 使用: venv\Scripts\activate
pip install -r requirements.txt
```

3. 数据库迁移

```bash
python manage.py migrate
```

4. 创建超级用户

```bash
python manage.py createsuperuser
```

5. 运行开发服务器

```bash
python manage.py runserver
```

6. 访问网站
   - 前台: http://127.0.0.1:8000/
   - 后台管理: http://127.0.0.1:8000/admin/

## 部署指南

项目支持使用Gunicorn和Whitenoise进行部署，详细部署步骤请参考Django官方文档。

## 贡献指南

欢迎提交Issue或Pull Request来改进项目。

## 许可证

本项目采用MIT许可证。