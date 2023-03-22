from django.forms import ModelForm
from .models import Topico, Conteudo, Conversor, Limite


class TopicoForm(ModelForm):
    class Meta:
        model = Topico
        fields = '__all__'

class ConteudoForm(ModelForm):
    class Meta:
        model = Conteudo
        fields = '__all__'

class ConversorForm(ModelForm):
    class Meta:
        model = Conversor
        fields = '__all__'

class LimiteForm(ModelForm):
    class Meta:
        model = Limite
        fields = '__all__'       