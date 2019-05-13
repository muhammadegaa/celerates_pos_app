from django.db import models
from django.contrib.contenttypes import fields
from django.utils import timezone

class Item(models.Model): 
	itemId = models.AutoField(primary_key=True)
	itemName = models.CharField(max_length=512)
	itemDesc = models.TextField(null=True)
	itemPrice = models.FloatField(null=True)
	itemQuantity = models.IntegerField(null=True)
	isDelete = models.BooleanField(default=False)
	createdDate = models.DateTimeField(editable=False)
	lastModifiedDate = models.DateTimeField(null=True)

	def save(self,*args,**kwargs):
		if not self.itemId:
			self.createdDate = timezone.now()
		else:
			self.lastModifiedDate = timezone.now()
		return super(Item, self).save(*args,**kwargs)

	class Meta:
		db_table = 'item'
