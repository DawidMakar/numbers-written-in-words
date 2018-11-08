from django.urls import path

from core.views import NumberToWordsView, ResultView

urlpatterns = [
    path('', NumberToWordsView.as_view(), name='number_to_words'),
    path('result/', ResultView.as_view(), name='result')
]