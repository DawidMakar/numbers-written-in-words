from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from core.forms import NumberToWordsForm
from core.utils import convert_number_to_words


class NumberToWordsView(FormView):

    form_class = NumberToWordsForm
    template_name = 'number_to_words.html'
    result = ''

    def form_valid(self, form):
        number = form.cleaned_data['number']
        self.result = convert_number_to_words(number)
        return super().form_valid(form)

    def get_success_url(self):
        self.success_url = f"{reverse_lazy('result')}?res={self.result}"
        return super().get_success_url()


class ResultView(TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        number_as_words = self.request.GET.get('res')
        context['result'] = number_as_words
        return context
