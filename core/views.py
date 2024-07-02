from typing import Any
from django.views.generic import TemplateView
from .models import Servico, Funcionario, Recurso, Preco

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any):
        context = super(IndexView, self).get_context_data(**kwargs)
        context ['servicos'] = Servico.objects.order_by('?').all() # ordena para mim
        context ['funcionarios'] = Funcionario.objects.order_by().all()
        context ['recursos_es'] = Recurso.objects.all()[0::2]
        context ['recursos_di'] = Recurso.objects.all()[1::2]
        context ['precos'] = Preco.objects.all()
        return context

