from django.db import models
from django.conf import settings
from django.utils.text import slugify

import os
from PIL import Image

from utils import utils


class Base(models.Model):

    """ Product database registration control """
    registration = models.DateField('Registration data', auto_now_add=True)
    modification = models.DateField('Modification data', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


class Product(Base):

    """ Product database fields """
    name = models.CharField(verbose_name='Name', max_length=60)
    short_description = models.TextField(verbose_name='Short description', max_length=60)
    long_description = models.TextField(verbose_name='Long description')
    image = models.ImageField(verbose_name='Image', upload_to='product_images/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(verbose_name='Slug', unique=True, blank=True, null=True, help_text="Don't need to type")
    price = models.FloatField(verbose_name='Price')
    promotional_price = models.FloatField(verbose_name='Promotional price', default=0)
    product_type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variable'),
            ('S', 'Simple'),
        )
    )

    def get_formatted_price(self):
        """ Return the formatted price to use in display admin """
        return utils.price_formatted(self.price)

    get_formatted_price.short_description = 'Price'

    def get_formatted_promotional_price(self):
        """ Return the formatted promotional price to use in display admin """
        return utils.price_formatted(self.promotional_price)

    get_formatted_promotional_price.short_description = 'Promotional Price'

    @staticmethod
    def resize_image(img, new_width=600):

        """ Resizing the original images from upload """
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=60,
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            """ Automated slug """
            slug = f'{slugify(self.name[:40])}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 600

        if self.image:
            self.resize_image(self.image, max_image_size)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.name


class Variation(models.Model):
    product = models.ForeignKey(Product, verbose_name='Product', related_name='variations', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='variation', max_length=50, blank=True, null=True)
    price = models.FloatField(verbose_name="Price")
    promotional_price = models.FloatField(verbose_name='Promotional price', default=0)
    inventory = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['product', 'name']
        ordering = ['pk']

    def __str__(self):
        return self.name or self.product.name


