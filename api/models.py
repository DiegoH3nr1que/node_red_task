from django.db import models

class Dados(models.Model):
    Sensor = models.BooleanField(default=False)
    Botao = models.BooleanField(default=False)
    LigaRobo = models.BooleanField(default=False)
    ResetContador = models.BooleanField(default=False)
    ValorContagem = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Lógica para definir LigaRobo como True se Sensor ou Botao forem acionados
        if self.Sensor or self.Botao:
            self.LigaRobo = True
            self.ValorContagem += 1
        else:
            self.LigaRobo = False
        
        # Lógica para resetar o contador
        if self.ResetContador:
            self.ValorContagem = 0  # Reseta o contador se ResetContador for True
        
        super(Dados, self).save(*args, **kwargs)

