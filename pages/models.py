from django.db import models

# Create your models here.




from django.db import models

# Create your models here.

class MainScrollModel(models.Model):
    image = models.ImageField(upload_to='main-scroll')
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=255)
    discount = models.PositiveSmallIntegerField()
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def str(self):
        return self.title
    



class Menu(models.Model):
    image = models.ImageField(upload_to='main-scroll')
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=255)
    price = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = 'scroll'
        verbose_name_plural = 'scrolls'