from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="category/image/")

    def __str__(self):
        return self.name
    

class Reklama(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="reklamalar")
    phone = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reklamalar")
    
    
    def __str__(self):
        return self.title
    
    @property
    def default_image(self):
        first_image = self.rasimlar.first()
        if first_image:
            return first_image.image.url
    
class ReklamaImages(models.Model):
    reklama = models.ForeignKey(Reklama, on_delete=models.CASCADE, related_name="rasimlar")
    image = models.ImageField(upload_to="reklama/resim/")
    def __str__(self):
        return f"{self.reklama.title} - {self.id}"
    
    
    