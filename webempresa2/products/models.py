from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here
class Category(models.Model):
    title = models.CharField(verbose_name='Categoría', max_length=225)
    slug = models.SlugField(verbose_name='Nombre corto',unique=True, blank=True, null=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='products', null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    @property
    def get_products(self):
        return Product.objects.filter(categories__title=self.title)


class Product(models.Model):
    productname = models.CharField(verbose_name='Nombre Producto',max_length=200)
    price = models.DecimalField(verbose_name='Precio', max_digits=15, decimal_places=0, null=True, blank = True)
    description = RichTextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='products', null=True, blank = True)
    pdf = models.FileField(verbose_name='PDF', upload_to='products/pdf', null=True, blank = True)
    categories = models.ForeignKey(Category, verbose_name='Categorías',related_name='Category', null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name='Unidades disponibles', default=0, null=True, blank = True)
    url = models.URLField(verbose_name='URL Mercadolibre',max_length=400, null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('product_detail', args=(self.id,))

    def __str__(self):
        return self.productname


class ProductImages(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE, related_name="imagenes")
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='products', null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación',null=True, blank = True)

    class Meta:
        verbose_name = 'imagen'
        verbose_name_plural = 'imagenes'

    def __str__(self):
        return str(self.product.productname)