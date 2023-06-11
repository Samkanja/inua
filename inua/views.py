from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.views.generic import TemplateView,ListView
from .models import Program,AboutUs,Activity


class HomePageView(ListView):
    template_name = 'homepage.html'
    model = Program
    context_object_name = 'programs'


class ActivityPageView(ListView):
    model = Activity
    template_name = 'activity.html'
    context_object_name =  'activitys'

    def get_queryset(self):
        program_slug = self.kwargs.get('program_slug')
       
        program = get_object_or_404(Program, slug=program_slug)
        queryset = super().get_queryset().filter(program = program)
        return queryset
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['program'] = self.program
        context['programs'] = Program.objects.all()
        return context



class AboutUsView(ListView):
    template_name = 'about.html'
    model = AboutUs
    context_object_name = 'aboutus'