from django.db import models

# Create your models here.
class CustomerReview(models.Model):
    name = models.CharField(max_length=100)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.name