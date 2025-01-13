from django.db import models

# Create your models here.
class Product(models.Model):
  # id # default primary key
  title = models.CharField(max_length=120) # max_length = (required)
  content = models.TextField(blank=True, null=True) # blank = (required), null = (optional) # blank=True: có thể để trống trong form, null=True: có thể để trống trong database
  price = models.DecimalField(decimal_places=2, max_digits=15, default=99.99)

  @property
  def sale_price(self):
    return "%.2f" % (float(self.price) * 0.8)
    # return f"{self.price * 0.8:.2f}"

  def get_discount(self):
    return "122"
