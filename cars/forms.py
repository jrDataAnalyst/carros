from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value= self.cleaned_data.get('value')
        if value < 10000:
            self.add_error('value', 'Valor minimo do Carro deve ser R$ 20.000')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1980:
            self.add_error('factory_year', "Não e possivel cadastrar carros com ano abaixo de 2010")
        return factory_year