from django.views.generic import ListView, TemplateView
from .models import Name, Subject

class homeviewpage(ListView):
    model = Name
    model = Subject
    template_name = 'home.html'


class mainviewpage(TemplateView):
    template_name = 'main.html'

# class homeviewpage(TemplateView):
#     template_name = 'home.html'

class aboutviewpage(TemplateView):
    template_name = 'about.html'

class contactviewpage(TemplateView):
    template_name = 'contact.html'

