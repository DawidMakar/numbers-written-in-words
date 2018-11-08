from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from core.forms import NumberToWordsForm
from core.utils import convert_number_to_words


class NumberToWordsView(FormView):

    form_class = NumberToWordsForm
    template_name = 'number_to_words.html'
    success_url = reverse_lazy('result')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        number = self.request.POST.get('number')
        if number == '':
            messages.error(request, 'Something went wrong!')
            return HttpResponseRedirect(reverse_lazy('number_to_words'))
        result = convert_number_to_words(number)
        return HttpResponseRedirect(f"{reverse_lazy('result')}?res={result}")


class ResultView(TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        number_as_words = self.request.GET.get('res')
        context['result'] = number_as_words
        return context
