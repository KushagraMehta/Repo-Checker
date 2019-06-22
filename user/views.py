from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
from .form import user_name


class home_page(TemplateView):
    template_name = "WELCOME_PAGE/index.html"

    def get(self, request):
        user_name_form = user_name()
        return render(request, self.template_name, {'form': user_name_form})

    def post(self, request):
        user_name_data = user_name(request.POST)

        if user_name_data.is_valid():
            print(user_name_data.cleaned_data['user'])
        return render(request, self.template_name)
