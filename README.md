# 智造科技网站

一个使用Django构建的科技企业网站，展示公司的研究成果、产品和服务。

## 功能特点

- 响应式设计，适应各种设备
- 公司信息展示
- 研究成果和技术动态
- 产品和服务介绍
- 在线联系表单

## 技术栈

- Django
- HTML5/CSS3
- JavaScript
- Bootstrap
- SQLite (开发) / PostgreSQL (生产)

## 安装与设置

1. 克隆仓库
```
git clone https://github.com/a135435/a135435.git
cd a135435
```

2. 创建并激活虚拟环境
```
python -m venv venv
source venv/bin/activate  # 在Windows上使用: venv\Scripts\activate
```

3. 安装依赖
```
pip install -r requirements.txt
```

4. 运行迁移
```
python manage.py migrate
```

5. 创建超级用户
```
python manage.py createsuperuser
```

6. 启动开发服务器
```
python manage.py runserver
```

## 项目结构

- `zhizao/` - 主项目目录
- `mainsite/` - 主站点应用
- `scienceApp/` - 科研成果展示应用
- `productApp/` - 产品展示应用
- `templates/` - HTML模板
- `static/` - 静态文件(CSS, JS, 图片)