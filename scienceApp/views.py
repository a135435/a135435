from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Direction, Research, Member
from django.db.models import Count


class HomeView(ListView):
    """首页视图"""
    model = Research
    template_name = 'science/home.html'
    context_object_name = 'featured_researches'
    
    def get_queryset(self):
        return Research.objects.filter(is_featured=True).order_by('-publish_date')[:6]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directions'] = Direction.objects.annotate(
            research_count=Count('researches')
        ).order_by('-research_count')[:6]
        context['key_members'] = Member.objects.filter(is_key_member=True).order_by('order')[:4]
        return context


class ResearchListView(ListView):
    """科研成果列表视图"""
    model = Research
    template_name = 'science/research_list.html'
    context_object_name = 'researches'
    paginate_by = 9
    
    def get_queryset(self):
        if 'direction' in self.kwargs:
            self.direction = get_object_or_404(Direction, slug=self.kwargs['direction'])
            return Research.objects.filter(direction=self.direction).order_by('-publish_date')
        return Research.objects.all().order_by('-publish_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directions'] = Direction.objects.annotate(
            research_count=Count('researches')
        ).order_by('-research_count')
        
        if 'direction' in self.kwargs:
            context['current_direction'] = self.direction
            
        return context


class ResearchDetailView(DetailView):
    """科研成果详情视图"""
    model = Research
    template_name = 'science/research_detail.html'
    context_object_name = 'research'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        research = self.get_object()
        
        # 获取相同方向的其他科研成果
        context['related_researches'] = Research.objects.filter(
            direction=research.direction
        ).exclude(id=research.id).order_by('-publish_date')[:3]
        
        return context


class DirectionDetailView(DetailView):
    """研究方向详情视图"""
    model = Direction
    template_name = 'science/direction_detail.html'
    context_object_name = 'direction'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        direction = self.get_object()
        
        # 获取该方向的所有科研成果
        context['researches'] = Research.objects.filter(
            direction=direction
        ).order_by('-publish_date')
        
        return context


class TeamView(ListView):
    """团队成员视图"""
    model = Member
    template_name = 'science/team.html'
    context_object_name = 'members'
    
    def get_queryset(self):
        return Member.objects.all().order_by('order', 'name')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key_members'] = Member.objects.filter(is_key_member=True).order_by('order')
        context['other_members'] = Member.objects.filter(is_key_member=False).order_by('order')
        return context


def about_view(request):
    """关于我们视图"""
    return render(request, 'science/about.html')