from django.forms import ModelForm
from wine_app.models import Wine

class WineForm(ModelForm):
    class Meta:
        model = Wine
        fields = ('wine_name', 'price', 'varietal', 'description')