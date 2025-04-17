# 科研管理系统

基于Django开发的科研项目管理系统，用于展示和管理研究方向、研究项目、研究成果等。

## 功能特点

- 用户注册与登录
- 研究方向管理
- 研究项目展示
- 研究成果发布
- 科研动态分享
- 响应式设计，支持多设备访问

## 技术栈

- Django 4.2
- Python 3.9+
- HTML5/CSS3
- JavaScript

## 安装

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

6. 启动开发服务器
```bash
python manage.py runserver
```

## 使用

访问 http://127.0.0.1:8000/ 查看网站首页
访问 http://127.0.0.1:8000/admin/ 进入管理后台