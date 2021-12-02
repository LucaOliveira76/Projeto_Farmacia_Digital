from django.contrib import admin
from .models import Medicamento
from .models import Receita

admin.site.register(Medicamento)
admin.site.register(Receita)
