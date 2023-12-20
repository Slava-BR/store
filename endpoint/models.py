from django.db import models

from endpoint.Validators import percent_is_valid

SIZES = dict({'size': []})
TYPES = {'Hoodie': 'Худи', 'Sweatshirts': 'Свитшоты', 'T-shirts': 'Футболки', 'Longsleeve': 'Лонгсливы', }
COLLECTIONS = {'VSRAP': 'VSRAP', 'CMH': 'CMH'}
TEXTILE = {'Cooler': 'кулирка'}
MATERIALS = {'Cotton': 'Хлопок'}


# Create your models here.
class Cloth(models.Model):
    main = models.BooleanField()
    title = models.CharField(primary_key=True, max_length=100)
    sale = models.PositiveSmallIntegerField(validators=[percent_is_valid, ])
    image = models.ImageField(upload_to='image/%Y/%m/%d/', blank=False)
    size = models.JSONField(default=SIZES, blank=False)
    type = models.CharField(choices=TYPES, blank=False, max_length=30)
    collections = models.CharField(choices=COLLECTIONS, blank=False, max_length=30)
    textile = models.CharField(choices=TEXTILE, blank=False, max_length=30)
    material = models.CharField(choices=MATERIALS, blank=False, max_length=30)
    price = models.PositiveIntegerField(blank=False, default=0)
    slug_title = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL_TITLE")