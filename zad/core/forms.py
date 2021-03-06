from django.forms import IntegerField, Form


class NumberToWordsForm(Form):

    class Meta:
        fields = ['number']

    number = IntegerField(min_value=-999999999999, max_value=999999999999, label='Enter a number below:', required=True)
