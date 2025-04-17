from django.urls import path
from . import views

app_name = 'science'

urlpatterns = [
    # 首页
    path('', views.HomeView.as_view(), name='home'),
    
    # 科研成果
    path('research/', views.ResearchListView.as_view(), name='research_list'),
    path('research/<slug:slug>/', views.ResearchDetailView.as_view(), name='research_detail'),
    
    # 研究方向
    path('direction/<slug:slug>/', views.DirectionDetailView.as_view(), name='direction_detail'),
    path('direction/<slug:direction>/research/', views.ResearchListView.as_view(), name='direction_research_list'),
    
    # 团队
    path('team/', views.TeamView.as_view(), name='team'),
    
    # 关于我们
    path('about/', views.about_view, name='about'),
]