from django.db import models

class Dados(models.Model):
    Sensor = models.BooleanField(default=False)
    Botao = models.BooleanField(default=False)
    LigaRobo = models.BooleanField(default=False)
    ResetContador = models.BooleanField(default=False)
    ValorContagem = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.ResetContador:
            if self.Botao or self.Sensor:
                ultimo_dado = Dados.objects.last()
                if ultimo_dado:  # Verifica se existe um último dado
                    self.ValorContagem = ultimo_dado.ValorContagem + 1
                else:
                    self.ValorContagem = 1  # ou comece de 1 se for o primeiro registro
        else:
            self.ValorContagem = 0
        super().save(*args, **kwargs)
