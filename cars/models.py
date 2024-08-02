from django.db import models



class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Car(models.Model):

    # variaveis estão em inglês
    
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200) #Modelo
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # Marca
    factory_year = models.IntegerField(blank=True, null=True) # Ano de fabricação
    model_year = models.IntegerField(blank=True, null=True) # Modelo ano
    plate = models.CharField(max_length=10, blank=True, null=True) #placa
    value = models.FloatField(blank=True, null=True) # Valor do carro
    photo = models.ImageField(upload_to='cars/', blank=True, null=True) # foto
    bio = models.TextField(blank=True, null=True)

    # OBS: blank e true possibilitam enviar dados sem adcionar nada nos campos

    def __str__(self):
        return self.model
    
class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.cars_count} - {self.cars_value}'

