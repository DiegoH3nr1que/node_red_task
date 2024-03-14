from django.db import models

class Dados(models.Model):
    Sensor = models.BooleanField(default=False)
    Botao = models.BooleanField(default=False)
    LigaRobo = models.BooleanField(default=False)
    ResetContador = models.BooleanField(default=False)
    ValorContagem = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if (self.Botao or self.Sensor) and not self.ResetContador:
            self.ValorContagem += 1
        elif self.ResetContador:
            self.ValorContagem = 0
        super().save(*args, **kwargs)
