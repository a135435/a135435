# 科研信息管理系统

一个基于Django的科研信息管理平台，用于管理和展示科研项目、成果和研究人员信息。

## 项目特点

- 科研项目管理与展示
- 研究成果跟踪与统计
- 研究人员信息管理
- 数据可视化展示
- 响应式设计，支持多设备访问

## 技术栈

- **后端**: Django 2.2.4
- **前端**: HTML5, CSS3, JavaScript, Chart.js
- **数据库**: SQLite (开发) / MySQL (生产)
- **图像处理**: Pillow

## 安装步骤

1. 克隆仓库
   ```bash
   git clone https://github.com/yourusername/science-app.git
   cd science-app
   ```

2. 创建并激活虚拟环境
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows使用: venv\Scripts\activate
   ```

3. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

4. 数据库迁移
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

## 使用说明

- 访问 `http://127.0.0.1:8000/` 浏览网站
- 访问 `http://127.0.0.1:8000/admin/` 进入管理后台

## 项目结构

```
science-app/
├── manage.py
├── scienceApp/         # 主应用
│   ├── admin.py        # 管理后台配置
│   ├── models.py       # 数据模型
│   ├── views.py        # 视图函数
│   ├── urls.py         # URL路由
│   ├── templates/      # HTML模板
│   └── static/         # 静态文件
└── science_project/    # 项目设置
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## 许可证

本项目采用MIT许可证，详情请查看LICENSE文件。