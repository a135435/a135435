# 智能科技企业网站

## 项目概述

智能科技企业网站是一个基于Django开发的现代化企业门户网站，采用多应用架构设计，致力于展示企业的产品、科研成果和服务能力。网站设计风格借鉴苹果官网的简约美学，结合了Bootstrap框架和自定义CSS，打造现代感强、响应式的用户体验。

## 特色功能

- 现代设计风格：采用渐变色、卡片式布局和精美动效
- 完全响应式：完美适配从手机到大屏显示器的各种设备
- 数据可视化：集成Chart.js实现科研成果数据的动态图表展示
- 模块化架构：采用Django多应用设计，实现功能模块化
- SEO友好：符合SEO最佳实践，提高搜索引擎可见性
- 管理后台：强大的Django管理界面，轻松管理网站内容

## 技术栈

- **后端**: 
  - Django 2.2.4
  - Python 3.x
  - SQLite (开发环境)

- **前端**: 
  - HTML5 / CSS3
  - Bootstrap 4.6
  - JavaScript / jQuery
  - Chart.js (数据可视化)
  - Font Awesome (图标库)

## 安装与部署

### 系统要求

- Python 3.6+
- pip (Python包管理器)
- 虚拟环境工具 (推荐使用virtualenv或venv)

### 安装步骤

1. **克隆项目仓库**

```bash
git clone https://github.com/a135435/a135435.git
cd a135435
```

2. **创建并激活虚拟环境**

```bash
# Windows系统
python -m venv venv
venv\Scripts\activate

# Linux/Mac系统
python3 -m venv venv
source venv/bin/activate
```

3. **安装依赖包**

```bash
pip install -r requirements.txt
```

4. **执行数据库迁移**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **创建超级管理员账号**

```bash
python manage.py createsuperuser
```

6. **启动开发服务器**

```bash
python manage.py runserver
```

## 作者

- 小黄

---

© 2024 智能科技有限公司. 保留所有权利.