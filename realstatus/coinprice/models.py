from django.db import models
from price.models import TimeStempedInitalization

# Create your models here.
class StockInformation(TimeStempedInitalization):
    pass

    class Meta:
        db_table: str = "stock_status"
