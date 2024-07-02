from typing import Any
from django.views.generic import FormView
from .models import Servico, Funcionario, Recurso, Preco
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs: Any):
        context = super(IndexView, self).get_context_data(**kwargs)
        context ['servicos'] = Servico.objects.order_by('?').all() # ordena para mim
        context ['funcionarios'] = Funcionario.objects.order_by().all()
        context ['recursos_es'] = Recurso.objects.all()[0::2]
        context ['recursos_di'] = Recurso.objects.all()[1::2]
        context ['precos'] = Preco.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o E-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
