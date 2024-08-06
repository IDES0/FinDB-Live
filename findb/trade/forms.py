from django import forms

class TradeForm(forms.Form):
    ticker = forms.CharField(label='Ticker Symbol', max_length=10)
    quantity = forms.IntegerField(label='Quantity')
    action = forms.ChoiceField(
        choices=[('buy', 'Buy'), ('sell', 'Sell')],
        widget=forms.RadioSelect,
        initial='buy',
        label='Action'
    )