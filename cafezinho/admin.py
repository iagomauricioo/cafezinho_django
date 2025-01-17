from django.contrib import admin
from cafezinho.models import Contribuicao, Contribuinte

class ContribuicaoAdmin(admin.ModelAdmin):
    list_display = ('contribuinte', 'descricao_da_contribuicao', 'data',)
    search_fields = ('contribuinte__nome', 'descricao_da_contribuicao', 'data',)

admin.site.register(Contribuicao, ContribuicaoAdmin)

class ContribuinteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Contribuinte, ContribuinteAdmin)
