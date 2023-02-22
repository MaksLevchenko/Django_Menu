from django.views.generic import TemplateView


class MenuIndexView(TemplateView):
    template_name = "menu/index.html"
