from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from main.models import Volonter, KindOfWork, Skill, Transport


class MainView(TemplateView):
    template_name = 'list_volonter.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context.update({
            'volonters': Volonter.objects.all(),
        })
        return context


class VolonterListView(ListView):
    template_name = 'list_volonter.html'
    model = Volonter
    context_object_name = 'volonters'

class VolonterDetailView(DetailView):
    template_name = 'view_volonter.html'
    model = Volonter
    context_object_name = 'volonter'

class VolonterCreateView(CreateView):
    template_name = 'create_volonter.html'
    model = Volonter
    fields = ('fio', 'address',
              'telephone', 'gender')
    success_url = reverse_lazy('list_volonters')

class VolonterUpdateView(UpdateView):
    template_name = 'update_volonter.html'
    model = Volonter
    context_object_name = 'volonter'
    fields = ('fio', 'address',
              'telephone', 'gender')

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class KindOfWorkMainView(TemplateView):
    template_name = 'list_kindofwork.html'
    def get_context_data(self, **kwargs):
        context = super(KindOfWorkMainView, self).get_context_data()
        context.update({'kWorks':KindOfWork.objects.all()})
        return context
class KindOfWorkListView(ListView):
    template_name = 'list_kindofwork.html'
    model = KindOfWork
    context_object_name = 'kWork'
class KindOfWorkDetailView(DetailView):
    template_name = 'view_kindofwork.html'
    model = KindOfWork
    context_object_name = 'kWork'
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class SkillMainView(TemplateView):
    template_name = 'list_skill.html'
    def get_context_data(self, **kwargs):
        context = super(SkillMainView, self).get_context_data()
        context.update({'skills': Skill.objects.all()})
        return context
class SkillListView(ListView):
    template_name = 'list_skill.html'
    model = Skill
    context_object_name = 'skills'
class SkillDetailView(DetailView):
    template_name = 'view_skill.html'
    model = Skill
    context_object_name = 'skill'
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class TransportMainView(TemplateView):
    template_name = 'list_transport.html'
    def get_context_data(self, **kwargs):
        context = super(TransportMainView, self).get_context_data()
        context.update({'trans': Transport.objects.all()})
        return context
class TransportListView(ListView):
    template_name = 'list_transport.html'
    model = Transport
    context_object_name = 'trans'
class TransportDetailView(DetailView):
    template_name = 'view_transport.html'
    model = Transport
    context_object_name = 'trans'

