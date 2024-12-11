from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
# Create your models here.

class Site(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='media',blank=True,null=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        code_img = qrcode.make(self.name)
        canva = Image.new('RGB',(310,310),'white')
        draw = ImageDraw.Draw(canva)
        canva.paste(code_img)
        filename = f'image-{self.name}.png'
        buffer = BytesIO()
        canva.save(buffer,'PNG')
        self.image.save(filename,File(buffer),save=False)
        canva.close()
        super().save(*args,**kwargs)


