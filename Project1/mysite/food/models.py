from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length= 200)
    item_desc = models.CharField(max_length= 200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default= 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.ukvisitorguide.cn%2Fwp-content%2Fuploads%2F2015%2F11%2FFood-placeholder.jpg&f=1&nofb=1')
