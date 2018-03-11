from django.db import models



# Create your models here.
class Cliente(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Direccion= models.CharField(max_length=50, null=True)
    Telefono= models.CharField(max_length=15)
    Email= models.CharField(max_length=50, null=True)
    Consumidor_Final=models.BooleanField(default=True)
    Empresa=models.BooleanField(default=False)

    def ClienteResumen(self):
    	cadena="{0} {1} ({2})"
    	return cadena.format(self.Nombre, self.Apellido,self.Telefono)


    def __str__(self):              # __unicode__ on Python 2
       return self.ClienteResumen()


class Vehiculo(models.Model):
    Marca= models.CharField(max_length=20)
    Modelo = models.CharField(max_length=20)
    Observacion = models.CharField(max_length=50, null=True)
    
    def VehiculoResumen(self):
    	cadena="{0} {1}"
    	return cadena.format(self.Marca, self.Modelo)

    def __str__(self):              # __unicode__ on Python 2
        return self.VehiculoResumen()

class Turno(models.Model):
	Cliente=models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
	Vehiculo=models.ForeignKey(Vehiculo, null=False, blank=False, on_delete=models.CASCADE)
	FechaIngreso=models.DateTimeField(auto_now=False)
	Patente=models.CharField(max_length=20)

	def __str__(self):
		cadena="{0} {1} {2} ==> {3}"
		return cadena.format(self.Cliente, self.Vehiculo, self.Patente, self.FechaIngreso)
