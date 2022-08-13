from django.db import models


class Supplier(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.name