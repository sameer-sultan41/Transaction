from django.db import models


# Create your models here.
class Transaction(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(
        max_length=10, 
        choices=(("CREDIT", "CREDIT"), ("DEBIT", "DEBIT"))
    )

    def save(self, *args, **kwargs):
        if self.transaction_type == "DEBIT":
            self.amount = -abs(self.amount)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title