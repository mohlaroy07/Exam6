from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.name
    
    

class Ad(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    owner = models.CharField(max_length=150)
    condition = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')
    phone = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.title} - {self.description}'