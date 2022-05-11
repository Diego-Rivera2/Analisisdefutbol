from django.db import models

# Create your models here.


#model.usuario

class usuarios(models.Model):
    id= models.AutoField(auto_created = True, primary_key = True)
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    direccion= models.CharField(max_length=40)
    fecha_nac= models.DateField(max_length=40)  
    pais= models.CharField(max_length=40)
    telef=models.CharField(max_length=40)
    correo=models.EmailField(max_length=40)
    usuario= models.CharField(max_length=40)
    password= models.CharField(max_length=40)
    perfil=models.CharField(max_length=40)
    imagen=models.CharField(max_length=80)

    def __str__(self):
        texto="{0}({1})"
        return texto.format(self.id,self.nombre,self.apellido,self.direccion,self.fecha_nac,self.pais,self.telef,self.correo,self.usuario,self.password,self.perfil,self.imagen)



#model.itens
class itens(models.Model):
    id=models.AutoField(auto_created = True, primary_key = True)
    nameItens= models.CharField(max_length=40)
    descripcion= models.CharField(max_length=40)

    def __str__(self):
         texto="{0}({1})"
         return texto.format(self.id,self.nameItens,self.descripcion)

     
#model.pages

class page(models.Model):
    id=models.AutoField(auto_created = True, primary_key = True)
    idUsuario= models.CharField(max_length=10)
    titulo= models.CharField(max_length=40)
    subtitulo= models.CharField(max_length=40)
    cuerpo= models.CharField(max_length=40)
    autor= models.CharField(max_length=40)
    fechaCreacion= models.DateField()  
    imagen=models.CharField(max_length=80)

    def __str__(self):
         texto="{0}({1})"
         return texto.format(self.id,self.idUsuario,self.titulo,self.subtitulo,self.cuerpo,self.autor,self.fechaCreacion,self.imagen,)


