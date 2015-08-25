from django.db import models
from django.utils.translation import ugettext as _


class Order(models.Model):
    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Order')
    amount = models.IntegerField(verbose_name=_('amount'), default=0)
