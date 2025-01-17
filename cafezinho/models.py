from django.db import models

class Contribuinte(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Contribuicao(models.Model):
    contribuinte = models.ForeignKey(Contribuinte, on_delete=models.CASCADE)
    descricao_da_contribuicao = models.CharField(max_length=100)
    data = models.DateField()
    class Meta:
        verbose_name = "Contribuição"
        verbose_name_plural = "Contribuições"
        ordering = ["data"]

    def __str__(self):
        return f"{self.contribuinte} - {self.descricao_da_contribuicao} - {self.data}"