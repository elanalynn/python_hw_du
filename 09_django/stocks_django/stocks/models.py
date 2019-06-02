# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Stock(models.Model):
    """A stock object"""

    symbol = models.CharField(max_length=4)
    date_added = models.DateTimeField(auto_now_add=True)
    purchasePrice = models.CharField
    currentPrice = models.CharField
    quantity = models.CharField
    purchaseDate = models.CharField

    def __str__(self):
        """Return a string representation of the model."""
        return {
            symbol: self.symbol,
            purchasePrice: self.purchasePrice,
            currentPrice: self.currentPrice,
            quantity: self.quantity,
            purchaseDate: self.purchaseDate,
        }

