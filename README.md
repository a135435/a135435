# 科研成果展示网站

一个基于Django开发的科研成果展示平台，用于展示研究项目、论文、团队成员及相关活动。

## 功能特点

- 科研项目展示
- 研究成果详情页
- 团队成员介绍
- 响应式设计，支持各种设备访问

## 技术栈

- Python 3.8+
- Django 4.2.4
- Bootstrap 5
- CKEditor (富文本编辑)
- Pillow (图像处理)
- Whitenoise (静态文件处理)

## 安装指南

1. 克隆仓库
```bash
git clone https://github.com/a135435/a135435.git
cd a135435
```

2. 创建虚拟环境并激活
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 运行迁移
```bash
python manage.py migrate
```

5. 创建超级用户
```bash
python manage.py createsuperuser
```

6. 运行开发服务器
```bash
python manage.py runserver
```

## 项目结构

```
project/
├── scienceApp/         # 主应用
│   ├── models.py       # 数据模型
│   ├── views.py        # 视图函数
│   ├── urls.py         # URL路由
│   ├── templates/      # HTML模板
│   └── static/         # 静态文件
├── media/              # 用户上传文件
├── manage.py           # Django管理脚本
└── requirements.txt    # 项目依赖
```

## 部署

本项目可以部署在任何支持Python的服务器上，推荐使用Gunicorn作为WSGI服务器。

## 许可证

MIT