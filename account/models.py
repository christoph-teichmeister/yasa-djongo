from ai_django_core.models import CommonInfo
from django.contrib.auth.models import AbstractUser
from django.db import models
from djongo.models import ObjectIdField


class User(CommonInfo, AbstractUser):
    # Abstract model for any user

    _id = ObjectIdField()

    name = models.CharField(max_length=50)
    rooms = models.ManyToManyField("room.Room", through="room.UserTransactionsForRoom")

    is_guest = models.BooleanField(default=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_guest and not self.is_superuser:
            self.email = f"{self._id}@{self.name}.local"
            self.username = f"{self.name}-{self._id}"

        super().save(*args, **kwargs)